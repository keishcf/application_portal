from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import SignupView as AllAuthSignUpView


class SignUpAdminView(AllAuthSignUpView):
    template_name = "account/signup_admin.html"
