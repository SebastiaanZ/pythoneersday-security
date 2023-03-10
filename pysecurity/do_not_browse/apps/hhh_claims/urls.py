from django import urls

from . import views

app_name = "hhh"
urlpatterns = [
    urls.path("", views.Priorities.as_view(), name="one"),
    urls.path(
        "download-service/privacy-data-user-<int:user_id>.txt",
        views.DownloadUserData.as_view(),
        name="user-data",
    ),
]
