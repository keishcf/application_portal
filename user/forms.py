from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
import logging
from django.shortcuts import resolve_url

logger = logging.getLogger(__name__)


class MyCustomSignupForm(SignupForm):
    is_applicant = forms.BooleanField(required=False, widget=forms.RadioSelect)
    is_manager = forms.BooleanField(required=False, widget=forms.RadioSelect)

    def save(self, request):

        user = super().save(request)
        user.is_applicant = self.cleaned_data["is_applicant"]
        user.is_manager = self.cleaned_data["is_manager"]
        user.save()
        if user.is_applicant:
            user.groups.add(1)

        if user.is_manager:
            user.groups.add(2)
        return user
