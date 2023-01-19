from django.shortcuts import render

# Create your views here.


def get_base_page(request):
    return render(request, 'goodlife/goodlife_base.html')
