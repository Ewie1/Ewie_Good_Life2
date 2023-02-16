from django.shortcuts import render
from django.views import generic, View
from goodlife.models import BookTrainer
from .forms import BookTrainerForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def get_base_page(request):
    return render(request, 'goodlife/goodlife_base.html')


def get_about_page(request):
    return render(request, 'goodlife/goodlife_train.html')


def book_trainer(request):
    booking = BookTrainerForm()

    if request.method == 'POST':
        booking = BookTrainerForm(request.POST)

        if booking.is_valid():
            reservation = booking.save(commit=True)
            reservation.save()
            messages.success(request, 'Your are booked in!')
            
    context = {
        'booking': booking
    }
    return render(request, 'goodlife/goodlife_index.html', context)
