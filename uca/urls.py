"""
URL configuration for uca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from siteuca import views
from django.contrib.auth import views as auth_views
from siteuca.views import VoluntarioCreateView, VoluntarioOKView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # público
    path("", views.home, name="home"),
    path("noticias/", views.NoticiaListView.as_view(), name="noticias_list"),
    path("integrantes/", views.IntegranteListView.as_view(), name="integrantes_list"),
    path("voluntarie-se/", VoluntarioCreateView.as_view(), name="voluntario_form"),
    path("voluntarie-se/obrigado/", VoluntarioOKView.as_view(), name="voluntario_ok"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)