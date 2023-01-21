from django.shortcuts import render
from .models import Photo

# Create your views here.


def get_base_page(request):
    return render(request, 'goodlife/goodlife_base.html')


def get_about_page(request):
    return render(request, 'goodlife/goodlife_train.html')