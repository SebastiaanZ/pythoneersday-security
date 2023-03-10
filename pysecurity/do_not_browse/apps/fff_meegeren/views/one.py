import logging
from typing import Any

import jwt
from django import http
from django.contrib.auth import mixins
from django.core import exceptions
from django.db import models as db_models
from django.views import generic

from .. import models

log = logging.getLogger(__name__)


class UserPassesTestOr404Mixin(mixins.UserPassesTestMixin):
    def handle_no_permission(self) -> http.HttpResponseRedirect:
        try:
            response = super().handle_no_permission()
        except exceptions.PermissionDenied as e:
            raise http.Http404("No notes matches the given query.") from e
        return response


class Nostradamus(UserPassesTestOr404Mixin, generic.TemplateView):
    template_name = "fff/one.html"

    def test_func(self) -> bool | None:
        session_key = self.request.session.session_key
        token = self.request.COOKIES.get("token")
        try:
            decoded_token = jwt.decode(
                token,
                key="very-secure-key-for-jwt",
                options={"verify_signature": True},
                algorithms=["HS256"],
            )
        except jwt.InvalidTokenError as e:
            log.exception(f"Invalid token found!")
            return False

        if decoded_token.get("session") != session_key:
            return False

        return decoded_token.get("user_id") == self.request.user.pk

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        query = kwargs.pop("query", None)
        q_object = db_models.Q(author_id=self.request.user.pk)
        if query:
            q_object &= db_models.Q(note__contains=query)

        qs = models.PrivateNoteFFF.objects.filter(q_object)
        return super().get_context_data(notes=list(qs), **kwargs)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        user_id = request.POST.get("user_id")
        query = request.POST.get("query")

        if not user_id:
            return http.HttpResponseBadRequest("No bueno!")

        context = self.get_context_data(query=query)
        return self.render_to_response(context)


class Note(UserPassesTestOr404Mixin, generic.DetailView):
    model = models.PrivateNoteFFF
    template_name = "fff/note.html"
    context_object_name = "note"

    def test_func(self) -> bool | None:
        session_key = self.request.session.session_key
        token = self.request.COOKIES.get("token")
        try:
            decoded_token = jwt.decode(
                token,
                key="very-secure-key-for-jwt",
                options={"verify_signature": False},
                algorithms=["HS256"],
            )
        except jwt.InvalidTokenError as e:
            log.exception(f"Invalid token found!")
            return False

        if decoded_token.get("session") != session_key:
            return False

        note = self.get_object()
        return decoded_token.get("user_id") == note.author_id
