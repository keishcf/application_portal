from django.urls import path, include
from django.views.generic import TemplateView
from apply.views import ApplicationListByUser, AddPersonalInformationView, AddAcademicBackgroundView, AddExtracurricularActivityView, AddDocumentView
urlpatterns = [
    
    path("", ApplicationListByUser.as_view(), name="index"),
    path("application/", include([
        path("personal-information/", AddPersonalInformationView.as_view(), name="add_personal_information"),
        path("academic-background/", AddAcademicBackgroundView.as_view(), name="add_academic_background"),
        path("extracurricular-activity/", AddExtracurricularActivityView.as_view(), name="add_extracurricular_activity"),
        path("document/", AddDocumentView.as_view(), name="add_document"),
    ])),

]
