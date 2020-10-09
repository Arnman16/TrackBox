"""trackbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from instrument.api import urls as api_urls
from rest_framework import routers
from users.api.views import UserViewSet
from django.views.generic import TemplateView



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name="home"),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
]
