from django.urls import path, include
from user.views import SignUpAdminView

urlpatterns = [
    path(
        "signup/admin/",
        SignUpAdminView.as_view(),
        name="account_signup_admin",
    ),
]
