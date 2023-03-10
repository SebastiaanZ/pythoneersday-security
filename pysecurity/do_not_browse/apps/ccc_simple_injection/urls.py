from django import urls

from . import views

app_name = "ccc"
urlpatterns = [
    urls.path("", views.SimpleInjectionView.as_view(), name="one"),
]
