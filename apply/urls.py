from django.urls import path, include
from django.views.generic import TemplateView
from apply.views import (
    DashboardView,
    AddPersonalInformationView,
    AddAcademicBackgroundView,
    AddExtracurricularActivityView,
    AddDocumentView,
    ManagerAllApplicationView,
    ApplicationDetailView,
    DeleteUserApplication,
    UserApplicationView,
    applicationPdf
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path(
        "applicant/",
        include(
            [
                path(
                    "personal-information/",
                    AddPersonalInformationView.as_view(),
                    name="add_personal_information",
                ),
                path(
                    "academic-background/",
                    AddAcademicBackgroundView.as_view(),
                    name="add_academic_background",
                ),
                path(
                    "extracurricular-activity/",
                    AddExtracurricularActivityView.as_view(),
                    name="add_extracurricular_activity",
                ),
                path("document/", AddDocumentView.as_view(), name="add_document"),
            ]
        ),
    ),
    path("<str:username>", UserApplicationView.as_view(), name="view_user_detail"),
    path("delete/<int:pk>", DeleteUserApplication.as_view(), name="delete_user_application"),
    path("pdf/<int:id>", applicationPdf, name="application_pdf")
]
