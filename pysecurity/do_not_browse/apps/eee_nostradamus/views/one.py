from typing import Any

from django import http
from django.contrib.auth import mixins
from django.db import models as db_models
from django.views import generic

from .. import models


class Nostradamus(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "eee/one.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        query = kwargs.pop("query", None)
        q_object = db_models.Q(author_id=self.request.user.pk)
        if query:
            q_object &= db_models.Q(note__contains=query)

        qs = models.PrivateNoteEEE.objects.filter(q_object)

        return super().get_context_data(notes=list(qs), **kwargs)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        user_id = request.POST.get("user_id")
        query = request.POST.get("query")

        if not user_id:
            return http.HttpResponseBadRequest("No bueno!")

        context = self.get_context_data(query=query)
        return self.render_to_response(context)


class Note(generic.DetailView):
    model = models.PrivateNoteEEE
    template_name = "eee/note.html"
    context_object_name = "note"
