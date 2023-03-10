from django import urls

from . import views

app_name = "core"
urlpatterns = [
    urls.path("", views.Index.as_view(), name="index"),
    urls.path("login/", views.LogIn.as_view(), name="login"),
    urls.path("logout/", views.LogOut.as_view(), name="logout"),
    urls.path("profile/", views.UserProfile.as_view(), name="profile"),
]
