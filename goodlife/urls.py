from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.get_base_page, name='get_base_page'),
    path('accounts/', include('allauth.urls')),
    path('goodlife_train.html', views.get_about_page, name='get_about_page'),
    path('goodlife_index.html', views.book_trainer, name='book_trainer'),
]
