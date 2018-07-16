from django.shortcuts import render
from django.http import HttpResponse
from .models import Announcement

# Create your views here.

def index(request):
    latest_announcement_list = Announcement.objects.order_by('-pub_date')[:4]
    context = {
        'latest_announcement_list' : latest_announcement_list,
    }
    return (request, 'home/index.html', context)
