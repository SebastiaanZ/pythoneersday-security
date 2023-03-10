from typing import Any

from django import http
from django.contrib.auth import mixins
from django.views import generic

from .. import models


class SimpleInjectionView(mixins.LoginRequiredMixin, generic.TemplateView):
    """The Tutorial view."""

    template_name = "ccc/one.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user_id = kwargs.pop("user_id", self.request.user.pk)
        query = kwargs.pop("query", None)

        if query:
            qs = models.PrivateNote.objects.filter(
                author_id=user_id, note__contains=query
            )
        else:
            qs = models.PrivateNote.objects.filter(author_id=user_id)
        return super().get_context_data(notes=qs, **kwargs)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        user_id = request.POST.get("user_id")
        query = request.POST.get("query")

        if not user_id:
            return http.HttpResponseBadRequest("No bueno!")

        context = self.get_context_data(user_id=user_id, query=query)
        return self.render_to_response(context)
