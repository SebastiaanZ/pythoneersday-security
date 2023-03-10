from django import urls

from . import views

app_name = "eee"
urlpatterns = [
    urls.path("", views.Nostradamus.as_view(), name="one"),
    urls.path("note/<int:pk>/", views.Note.as_view(), name="detail"),
]
