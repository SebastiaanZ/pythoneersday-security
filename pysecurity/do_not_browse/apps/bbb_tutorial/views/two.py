import traceback
from typing import Any

from django import db, http
from django.views import generic

from .. import models


class TutorialTwoView(generic.TemplateView):
    """The Tutorial view."""

    template_name = "tutorial/two.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        author_filter = kwargs.pop("author_filter", None)
        if author_filter:
            queryset = models.TutorialTwoNote.objects.raw(
                f"""
                SELECT * FROM tutorial_tutorialtwonote
                WHERE classification='PUB'
                AND author='{author_filter}'
                """
            )
        else:
            queryset = models.TutorialTwoNote.objects.raw(
                """
                SELECT * FROM tutorial_tutorialtwonote
                WHERE classification='PUB'
                """
            )
        notes = None
        try:
            notes = list(queryset)
        except db.DatabaseError as exception:
            db_error = "".join(traceback.format_exception(exception))
        else:
            db_error = None

        return super().get_context_data(**kwargs, notes=notes, db_error=db_error)

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        """Check if the value was modified."""
        author_filter = request.POST.get("author_filter", None)
        context = self.get_context_data(author_filter=author_filter)
        return self.render_to_response(context)
