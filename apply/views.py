from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from apply.models import UserApplication, ApplicantPersonalInformation, ApplicantAcademicBackground, ApplicantExtracurricularActivity, ApplicantDocument
from apply.forms import PersonalInformationForm, AcademicBackgroundForm, ExtracurricularActivityForm, DocumentForm
from django import views
from django.contrib import messages

class ApplicationListByUser(LoginRequiredMixin, views.generic.ListView):
    template_name = "apply/index.html"
    context_object_name = "applications"
    
    def get_queryset(self):
        return UserApplication.objects.filter(user=self.request.user)

class AddPersonalInformationView(LoginRequiredMixin, views.View):
    template_name = "apply/personal_information.html"
    
    def get(self, request):
        try:
            self.application , created= UserApplication.objects.get_or_create(user=self.request.user)
            try:
                personal_info = ApplicantPersonalInformation.objects.get(application=self.application)
                form = PersonalInformationForm(instance=personal_info)
            except ApplicantPersonalInformation.DoesNotExist:
                form = PersonalInformationForm()
        except ApplicantPersonalInformation.DoesNotExist:
            form = PersonalInformationForm()
        
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):    
        try:
            instance = ApplicantPersonalInformation.objects.get(application__user=request.user)
            form = PersonalInformationForm(request.POST, instance=instance)
        except ApplicantPersonalInformation.DoesNotExist:
            form = PersonalInformationForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(user=self.request.user)
            personal_info.save()
            return redirect('add_academic_background') 

        return render(request, self.template_name, {'form': form})
    
class AddAcademicBackgroundView(views.View):
    template_name = "apply/academic_background.html"
    
    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                personal_info = ApplicantAcademicBackground.objects.get(application=self.application)
                form = AcademicBackgroundForm(instance=personal_info)
            except ApplicantAcademicBackground.DoesNotExist:
                form = AcademicBackgroundForm()
        except ApplicantAcademicBackground.DoesNotExist:
            form = AcademicBackgroundForm()
        
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):    
        try:
            instance = ApplicantAcademicBackground.objects.get(application__user=request.user)
            form = AcademicBackgroundForm(request.POST, instance=instance)
        except ApplicantAcademicBackground.DoesNotExist:
            form = AcademicBackgroundForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(user=self.request.user)
            personal_info.save()
            return redirect('add_extracurricular_activity') 

        return render(request, self.template_name, {'form': form})
    

class AddExtracurricularActivityView(views.View):
    template_name = "apply/extracurricular_activity.html"
    
    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                personal_info = ApplicantExtracurricularActivity.objects.get(application=self.application)
                form = ExtracurricularActivityForm(instance=personal_info)
            except ApplicantExtracurricularActivity.DoesNotExist:
                form = ExtracurricularActivityForm()
        except ApplicantExtracurricularActivity.DoesNotExist:
            form = ExtracurricularActivityForm()
        
        return render(request, self.template_name, {"form": form})

    def post(self, request):    
        try:
            instance = ApplicantExtracurricularActivity.objects.get(application__user=request.user)
            form = ExtracurricularActivityForm(request.POST, instance=instance)
        except ApplicantExtracurricularActivity.DoesNotExist:
            form = ExtracurricularActivityForm(request.POST)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(user=self.request.user)
            personal_info.save()
            return redirect('add_document') 

        return render(request, self.template_name, {'form': form})

class AddDocumentView(views.View):
    template_name = "apply/document.html"
    
    def get(self, request):
        try:
            self.application = UserApplication.objects.get(user=self.request.user)
            try:
                personal_info = ApplicantDocument.objects.get(application=self.application)
                form = DocumentForm(instance=personal_info)
            except ApplicantDocument.DoesNotExist:
                form = DocumentForm()
        except ApplicantDocument.DoesNotExist:
            form = DocumentForm()
        
        return render(request, self.template_name, {"form": form})

    def post(self, request):    
        try:
            instance = ApplicantDocument.objects.get(application__user=request.user)
            form = DocumentForm(request.POST, request.FILES, instance=instance)
        except ApplicantDocument.DoesNotExist:
            form = DocumentForm(request.POST)

        if form.is_valid():
            messages.success(request, "Application Submitted Successfully")
            personal_info = form.save(commit=False)
            personal_info.application = UserApplication.objects.get(user=self.request.user)
            personal_info.save()
            return redirect('index') 

        return render(request, self.template_name, {'form': form})
