from typing import Any

from django import http
from django.contrib.auth import mixins
from django.views import generic

from .. import models


class SimpleSQLInjectionView(mixins.LoginRequiredMixin, generic.TemplateView):
    """The Tutorial view."""

    template_name = "ddd/one.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        author_id = self.request.user.pk
        query = kwargs.pop("query", None)
        if query:
            sql = rf"""
            SELECT * FROM simple_sql_injection_privatenoteddd WHERE note LIKE '%{query}%' ESCAPE '\' AND author_id = {author_id}
            """
            qs = models.PrivateNoteDDD.objects.raw(sql)
        else:
            qs = models.PrivateNoteDDD.objects.filter(author_id=author_id)
        return super().get_context_data(notes=list(qs), **kwargs)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        user_id = request.POST.get("user_id")
        query = request.POST.get("query")

        if not user_id:
            return http.HttpResponseBadRequest("No bueno!")

        context = self.get_context_data(query=query)
        return self.render_to_response(context)
