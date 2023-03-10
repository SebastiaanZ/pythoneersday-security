"""pysecurity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import conf, urls
from django.conf.urls.static import static
from django.contrib import admin
from django.templatetags.static import static as reverse_static
from django.views.generic import base

urlpatterns = [
    urls.path("admin/", admin.site.urls),
    urls.path("accounts/", urls.include("django.contrib.auth.urls")),
    urls.path("", urls.include("apps.aaa_core.urls")),
    urls.path("tutorial/", urls.include("apps.bbb_tutorial.urls")),
    urls.path("ccc/", urls.include("apps.ccc_simple_injection.urls")),
    urls.path("ddd/", urls.include("apps.ddd_simple_sql_injection.urls")),
    urls.path("eee/", urls.include("apps.eee_nostradamus.urls")),
    urls.path("fff/", urls.include("apps.fff_meegeren.urls")),
    urls.path("ggg/", urls.include("apps.ggg_priorities.urls")),
    urls.path("hhh/", urls.include("apps.hhh_claims.urls")),
    urls.path(
        "favicon.ico",
        base.RedirectView.as_view(url=reverse_static("favicon.ico"), permanent=True),
    ),
] + static(conf.settings.STATIC_URL, document_root=conf.settings.STATIC_ROOT)
