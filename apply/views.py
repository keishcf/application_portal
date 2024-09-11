from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import FileResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apply.models import (
    UserApplication,
    ApplicantPersonalInformation,
    ApplicantAcademicBackground,
    ApplicantExtracurricularActivity,
    ApplicantDocument,
)
from apply.forms import (
    PersonalInformationForm,
    AcademicBackgroundForm,
    ExtracurricularActivityForm,
    DocumentForm,
)
from django import views
from django.contrib import messages
from reportlab.pdfgen import canvas


class DashboardView(LoginRequiredMixin, views.generic.ListView):
    context_object_name = "user_application"
    paginate_by = 2

    def get_queryset(
        self,
    ):
        queryset = UserApplication.objects.all()
        if self.request.user.is_applicant:
            self.paginate_by = None
            try:
                queryset = UserApplication.objects.get(user=self.request.user.id)
            except ObjectDoesNotExist:
                queryset = []
        return queryset




    def get_template_names(self) -> list[str]:
        if self.request.user.is_manager:
            return "apply/manager.html"
        elif self.request.user.is_applicant:
            return "apply/applicant.html"


def applicationPdf(request, id):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    
    user_application = UserApplication.objects.get(user=id)
    p.drawString(100, 750, f"{user_application.user.username} Application")
    
    y = 700
    
    p.drawString(100, 300, f"{user_application.personal_information.first_name}")
    p.drawString(100, 400, f"{user_application.personal_information.last_name}")
    p.drawString(100, 500, f"{user_application.personal_information.bio}")
    p.drawString(100, 600, f"{user_application.personal_information.date_of_birth}")
    p.drawString(100, 800, f"{user_application.personal_information.phone_number}")
    p.drawString(100, 900, f"{user_application.personal_information.address}")
    p.showPage()
    p.save()
    
    buffer.seek(0)
    
    return FileResponse(buffer, as_attachment=True, filename=user_application.user.username + ".pdf")
    
    
    
    
    
    
    

class ApplicantView(LoginRequiredMixin, views.generic.ListView):
    template_name = "apply/applicant.html"
    context_object_name = "user_application"

    def get_queryset(self):
        return UserApplication.objects.filter(user=self.request.user)


class AddPersonalInformationView(
    LoginRequiredMixin, PermissionRequiredMixin, views.View
):
    permission_required = [
        "apply.add_user_application",
        "apply.change_user_application",
    ]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/personal_information.html"

    def get(self, request):
        try:
            self.application, created = UserApplication.objects.get_or_create(
                user=self.request.user
            )
            try:
                personal_info = ApplicantPersonalInformation.objects.get(
                    application=self.application
                )
                form = PersonalInformationForm(instance=personal_info)
            except ApplicantPersonalInformation.DoesNotExist:
                form = PersonalInformationForm()
        except ApplicantPersonalInformation.DoesNotExist:
            form = PersonalInformationForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        try:
            instance = ApplicantPersonalInformation.objects.get(
                application__user=request.user
            )
            form = PersonalInformationForm(request.POST, instance=instance)
        except ApplicantPersonalInformation.DoesNotExist:
            form = PersonalInformationForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(
                user=self.request.user
            )
            personal_info.save()
            return redirect("add_academic_background")

        return render(request, self.template_name, {"form": form})


class AddAcademicBackgroundView(
    LoginRequiredMixin, PermissionRequiredMixin, views.View
):
    permission_required = [
        "apply.add_user_application",
        "apply.change_user_application",
    ]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/academic_background.html"

    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                personal_info = ApplicantAcademicBackground.objects.get(
                    application=self.application
                )
                form = AcademicBackgroundForm(instance=personal_info)
            except ApplicantAcademicBackground.DoesNotExist:
                form = AcademicBackgroundForm()
        except UserApplication.DoesNotExist:
            form = AcademicBackgroundForm()
            return redirect("add_personal_information")

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        try:
            instance = ApplicantAcademicBackground.objects.get(
                application__user=request.user
            )
            form = AcademicBackgroundForm(request.POST, instance=instance)
        except ApplicantAcademicBackground.DoesNotExist:
            form = AcademicBackgroundForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(
                user=self.request.user
            )
            personal_info.save()
            return redirect("add_extracurricular_activity")

        return render(request, self.template_name, {"form": form})


class AddExtracurricularActivityView(
    LoginRequiredMixin, PermissionRequiredMixin, views.View
):
    permission_required = [
        "apply.add_user_application",
        "apply.change_user_application",
    ]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/extracurricular_activity.html"

    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                personal_info = ApplicantExtracurricularActivity.objects.get(
                    application=self.application
                )
                form = ExtracurricularActivityForm(instance=personal_info)
            except ApplicantExtracurricularActivity.DoesNotExist:
                form = ExtracurricularActivityForm()

        except UserApplication.DoesNotExist:
            form = ExtracurricularActivityForm()
            return redirect("add_personal_information")

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        try:
            instance = ApplicantExtracurricularActivity.objects.get(
                application__user=request.user
            )
            form = ExtracurricularActivityForm(request.POST, instance=instance)
        except ApplicantExtracurricularActivity.DoesNotExist:
            form = ExtracurricularActivityForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(
                user=self.request.user
            )
            personal_info.save()
            return redirect("add_document")

        return render(request, self.template_name, {"form": form})


class AddDocumentView(LoginRequiredMixin, PermissionRequiredMixin, views.View):
    permission_required = [
        "apply.add_user_application",
        "apply.change_user_application",
    ]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/document.html"

    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                applicant_document = ApplicantDocument.objects.get(
                    application=self.application
                )
                form = DocumentForm(instance=applicant_document)
            except ApplicantDocument.DoesNotExist:
                form = DocumentForm()
        except UserApplication.DoesNotExist:
            form = DocumentForm()
            return redirect("add_personal_information")

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        try:
            instance = ApplicantDocument.objects.get(application__user=request.user)
            form = DocumentForm(request.POST, request.FILES, instance=instance)
        except ApplicantDocument.DoesNotExist:
            form = DocumentForm(request.POST)

        if form.is_valid():
            application = UserApplication.objects.get(user=self.request.user)
            applicant_document = form.save(commit=False)
            applicant_document.application = UserApplication.objects.get(
                user=self.request.user
            )
            application.is_draft = False
            application.save()
            applicant_document.save()
            messages.success(request, "Application Submitted Successfully")
            return redirect("dashboard")

        return render(request, self.template_name, {"form": form})


# manager Views


class UserApplicationView(
    LoginRequiredMixin, PermissionRequiredMixin, views.generic.DetailView
):
    permission_required = ["apply.delete_user_application"]
    permission_denied_message = "Your Have no access to this resources"
    context_object_name = "user_application"
    template_name = "apply/user_application_detail.html"

    def get_object(self):
        username = get_object_or_404(get_user_model(), username=self.kwargs["username"])
        user = get_object_or_404(UserApplication, user=username)
        return user


class ManagerAllApplicationView(
    LoginRequiredMixin, PermissionRequiredMixin, views.generic.ListView
):
    model = UserApplication
    permission_required = ["apply.delete_user_application"]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/manager.html"
    context_object_name = "user_application"


class ApplicationDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, views.generic.DetailView
):
    model = UserApplication
    permission_required = ["delete_user_application"]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "apply/all_application_view.html"


class DeleteUserApplication(
    LoginRequiredMixin, PermissionRequiredMixin, views.generic.DeleteView
):
    model = UserApplication
    permission_required = ["apply.delete_user_application"]
    permission_denied_message = "You're not allowed to view this page"
    template_name = "snippet/delete_application.html"
    context_object_name = "user_application"
    
    # def get_object(self, *args, **kwargs):
    #     username = kwargs.get("username")
    #     queryset = get_object_or_404(UserApplication, user=username.id)
    #     return queryset
    
    def get_success_url(self, *args, **kwargs):
        pass
    
    def form_valid(self, form):
        messages.success(self.request, "Application Successfully Deleted")
        return super().form_valid(form)
    