from django import urls

from . import views

app_name = "tutorial"
urlpatterns = [
    urls.path("", views.TutorialOneView.as_view(), name="one"),
    urls.path("two/", views.TutorialTwoView.as_view(), name="two"),
]
