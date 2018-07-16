from django.shortcuts import render
from django.http import HttpResponse
from .models import Announcement

# Create your views here.

def index(request):
    latest_announcements = Announcement.objects.order_by('-pub_date')[:3]
    context = {
        'latest_announcements':latest_announcements,
    }
    return render(request, 'home/index.html', context)
