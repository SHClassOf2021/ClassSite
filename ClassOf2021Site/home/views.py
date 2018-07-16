from django.shortcuts import render
from django.http import HttpResponse
from .models import Announcement

# Create your views here.

def index(request):
    latest_announcements = Announcement.objects.order_by('-pub_date')[:3]
    context = {
<<<<<<< HEAD
        'latest_announcements' : latest_announcements,
    }
    return render(request, 'home/index.html', context)

def announcements(request):
    latest_announcements_all = Announcement.objects.order_by('-pub_date')[:]
    context = {
        'latest_announcements_all' : latest_announcements_all,
    }
    return render(request, 'home/announcements.html', context)
=======
        'latest_announcements':latest_announcements,
    }
    return render(request, 'home/index.html', context)
>>>>>>> 56f7fc63966f00dbe384c3108f0386d2ae3d279c
