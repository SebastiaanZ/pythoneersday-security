import datetime
from typing import Any

import jwt
from django import http
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins
from django.contrib.auth import views as auth_views
from django.views import generic


class Index(generic.TemplateView):
    """The index view."""

    template_name = "core/index.html"


class LogIn(auth_views.LoginView):
    """The log in view."""

    template_name = "core/login.html"

    def form_valid(self, form: auth_forms.AuthenticationForm) -> http.HttpResponse:
        response = super().form_valid(form)
        response.set_cookie(
            "token",
            jwt.encode(
                {
                    "user_id": self.request.user.pk,
                    "session": self.request.session.session_key,
                },
                "very-secure-key-for-jwt",
                algorithm="HS256",
            ),
            max_age=datetime.timedelta(days=7),
        )
        return response


class LogOut(auth_views.LogoutView):
    def post(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        response = super().post(request, *args, **kwargs)
        response.delete_cookie("token")
        return response


class UserProfile(mixins.LoginRequiredMixin, generic.TemplateView):
    """The user profile view."""

    template_name = "core/profile.html"
