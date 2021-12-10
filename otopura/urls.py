"""sofutomo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include, re_path
from . import settings
from django.conf.urls.static import static
from otopuraapp import apis
from rest_auth.registration.views import VerifyEmailView
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(apis.router.urls)),
    path('views/',include('otopuraapp.urls')),

    #SPA用
    path('home/', TemplateView.as_view(template_name='index.html')),
    path('account/<int:id>/', TemplateView.as_view(template_name='index.html')),
    path('signup/', TemplateView.as_view(template_name='index.html')),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('logout/', TemplateView.as_view(template_name='index.html')),
    path('upload/', TemplateView.as_view(template_name='index.html')),
    path('mypage/', TemplateView.as_view(template_name='index.html')),
    path('upload_list/', TemplateView.as_view(template_name='index.html')),
    path('good_list/', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),
    #re_path('.*', TemplateView.as_view(template_name='index.html'))
] + static (settings.MEDIA_URL, document_root=settings.MEDIA＿ROOT)