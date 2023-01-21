from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_base_page, name='get_base_page'),
    path('accounts/', include('allauth.urls')),
    path('goodlife_train.html', get_about_page, name='get_about_page'),
]
