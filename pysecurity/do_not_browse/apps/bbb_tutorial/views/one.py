from django import http
from django.views import generic


class TutorialOneView(generic.TemplateView):
    """The Tutorial view."""

    template_name = "tutorial/one.html"

    def post(self, request: http.HttpRequest) -> http.HttpResponse:
        """Check if the value was modified."""
        posted_value = request.POST.get("username", None)
        if posted_value is None:
            return http.HttpResponseBadRequest()

        status = "failure" if posted_value == "sebastiaan" else "success"
        context = self.get_context_data(status=status, posted_value=posted_value)
        return self.render_to_response(context)
