from django.http import HttpRequest
from django.urls import reverse

from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.core.internal.httpkit import get_frontend_url
from allauth.utils import build_absolute_uri


def send_unknown_account_mail(request: HttpRequest, email: str) -> None:
    if app_settings.EMAIL_UNKNOWN_ACCOUNTS:
        signup_url = get_signup_url(request)
        context = {
            "request": request,
            "signup_url": signup_url,
        }
        get_adapter().send_mail("account/email/unknown_account", email, context)


def get_signup_url(request: HttpRequest) -> str:
    url = get_frontend_url(request, "account_signup")
    if not url:
        url = build_absolute_uri(request, reverse("account_signup"))
    return url
