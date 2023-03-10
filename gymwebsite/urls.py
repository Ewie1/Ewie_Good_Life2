"""gymwebsite URL Configuration

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
from django.urls import path, include
from goodlife.views import get_base_page, get_about_page, book_trainer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_base_page, name='get_base_page'),
    path('accounts/', include('allauth.urls')),
    path('goodlife_train.html', get_about_page, name='get_about_page'),
    path('goodlife_index.html', book_trainer, name='book_trainer'),
]
