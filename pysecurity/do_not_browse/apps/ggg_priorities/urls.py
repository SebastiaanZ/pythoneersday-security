from django import urls

from . import views

app_name = "ggg"
urlpatterns = [
    urls.path("", views.Priorities.as_view(), name="one"),
]
