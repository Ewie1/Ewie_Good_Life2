from django.shortcuts import render
from django.views import generic, View
from .models import Photo
from .models import BookTrainer
from goodlife.models import BookTrainer
from .forms import BookTrainerForm

# Create your views here.


def get_base_page(request):
    return render(request, 'goodlife/goodlife_base.html')


def get_about_page(request):
    return render(request, 'goodlife/goodlife_train.html')


def book_trainer(request):
    booking = BookTrainerForm()
    context = {
        'booking': booking
    }
    return render(request, 'goodlife/goodlife_index.html', context)