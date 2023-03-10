import logging

from django import http
from django.contrib.auth import mixins
from django.views import generic

from .. import models

log = logging.getLogger(__name__)


class Priorities(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "ggg/one.html"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     query = kwargs.pop("query", None)
    #     q_object = db_models.Q(author_id=self.request.user.pk)
    #     if query:
    #         q_object &= db_models.Q(note__contains=query)
    #
    #     qs = models.PrioritizedNotes.objects.filter(q_object)
    #     return super().get_context_data(notes=list(qs), **kwargs)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        priority = request.POST.get("priority")
        if priority:
            qs = models.PrioritizedNotes.objects.raw(
                f"""
                SELECT * FROM priorities_prioritizednotes WHERE priority = '{priority}' AND author_id = {request.user.pk}
                """
            )
        else:
            qs = models.PrioritizedNotes.objects.filter(author_id=request.user.pk)

        serialized = [
            {
                "author": str(note.author),
                "priority": note.get_priority_display(),
                "note": note.note,
            }
            for note in qs
        ]

        return http.JsonResponse(serialized, safe=False)
