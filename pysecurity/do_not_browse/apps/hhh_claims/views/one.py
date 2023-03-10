import datetime
import io
import logging
from typing import Any

import jwt
from django import http, urls
from django.contrib.auth import mixins
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.views import generic

log = logging.getLogger(__name__)


class Priorities(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "hhh/one.html"

    @staticmethod
    def post(request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.JsonResponse:
        expiry = (timezone.now() + datetime.timedelta(minutes=5)).timestamp()
        user_id = request.user.pk
        user_data_url = urls.reverse("hhh:user-data", kwargs={"user_id": user_id})
        token = jwt.encode(
            {
                "user_id": user_id,
                "expiry": expiry,
                "claims": {
                    "allowed_download": user_data_url,
                },
            },
            "very-secure-download-token-key",
            algorithm="HS256",
        )
        reversed_token = "".join(reversed(token))
        return http.JsonResponse({"url": user_data_url, "token": reversed_token})


class DownloadUserData(mixins.LoginRequiredMixin, generic.View):
    def get(self, request: http.HttpRequest, user_id: int) -> http.FileResponse:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or not authorization_header.startswith("token "):
            return http.FileResponse(self._invalid_file())

        _, _, token = authorization_header.partition(" ")
        try:
            decoded_token = jwt.decode(
                token,
                key="very-secure-download-token-key",
                options={"verify_signature": False},
                algorithms=["HS256"],
            )
        except jwt.InvalidTokenError:
            return http.FileResponse(self._invalid_file())

        try:
            download_url = decoded_token["claims"]["allowed_download"]
        except KeyError:
            return http.FileResponse(self._invalid_file())
        if download_url != request.path:
            return http.FileResponse(self._invalid_file())

        try:
            token_user_id = decoded_token["user_id"]
        except KeyError:
            return http.FileResponse(self._invalid_file())
        if user_id != token_user_id:
            return http.FileResponse(self._invalid_file())

        match token_user_id:
            case 1:
                text = (
                    "Marvin's user data.\n\nThis is not the Paranoid Android you're"
                    " looking for."
                )
                file = io.BytesIO(text.encode("utf-8"))
            case 2:
                text = (
                    "Arthur's data!\n\nSecret code:"
                    " the-restaurant-at-the-end-of-the-workshop"
                )
                file = io.BytesIO(text.encode("utf-8"))
            case _:
                file = self._invalid_file()

        return http.FileResponse(file)

    def _invalid_file(self) -> io.BytesIO:
        return io.BytesIO("Error: This download is not valid".encode("utf-8"))
