from django import forms
from apply.models import (
    ApplicantAcademicBackground,
    ApplicantDocument,
    ApplicantExtracurricularActivity,
    ApplicantPersonalInformation,
    UserApplication,
)


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = ApplicantPersonalInformation
        exclude = ["id", "application"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "bio": forms.Textarea(attrs={"rows": 4, "cols": 15}),
        }
        labels = {
            "date_of_birth": "What is your birth date",
        }


class AcademicBackgroundForm(forms.ModelForm):
    class Meta:
        model = ApplicantAcademicBackground
        exclude = ["id", "application"]

        widgets = {
            "graduation_year": forms.DateInput(attrs={"type": "date"}),
            "degree": forms.Select(
                attrs={
                    "class": "py-3 px-4 pe-9 block w-full border-gray-900 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none"
                },
                choices=ApplicantAcademicBackground.DEGREE_CHOICES,
            ),
        }
        labels = {
            "institution_name": "Institution name you attended",
            "degree": "Your Degrees",
            "field_of_study": "What is your field of study ?",
            "graduation_year": "What year did you graduate",
            "start_year": "When did you start your institution year ?",
            "end_year": "When Did You Finish Your Institution Year ?",
        }


class ExtracurricularActivityForm(forms.ModelForm):
    class Meta:
        model = ApplicantExtracurricularActivity
        exclude = ["id", "application"]
        labels = {
            "activity_name": "What are extracurricular activities your performed ?",
        }
        widgets = {
            "start_year": forms.DateInput(),
            "end_year": forms.DateInput(),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ApplicantDocument
        exclude = ["id", "application"]
        widgets = {
            "cv": forms.FileInput(attrs={"accept": ".pdf"}),
            "transcript": forms.FileInput(attrs={"accept": ".pdf"}),
        }
        labels = {
            "cv": "Upload Your CV",
            "transcript": "Upload Your Transcript",
        }
