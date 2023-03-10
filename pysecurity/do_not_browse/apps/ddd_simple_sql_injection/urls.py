from django import urls

from . import views

app_name = "ddd"
urlpatterns = [
    urls.path("", views.SimpleSQLInjectionView.as_view(), name="one"),
]
