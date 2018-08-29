from django.shortcuts import render
from .models import Website
import random

# Create your views here.
def index(request):
    website_list = Website.objects.all()
    context = {
        'website_list': website_list,
    }
    return render(request, 'addsmanager/index.html', context)
