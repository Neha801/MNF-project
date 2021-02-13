from django.shortcuts import render
from .models import Video

# Create your views here.


def videos(request):
    video = Video.objects.all()
    return render(request, 'videos/videos.html', {"video": video})
