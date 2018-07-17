from django.shortcuts import render
from .models import Officer

# Create your views here.

def index(request):
    return render(request, 'contact/index.html')
