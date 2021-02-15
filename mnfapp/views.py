from django.shortcuts import render
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Scripts, Uploads
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from mnfapp.models import Uploads, Scripts

BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR, 'mnfapp/static/mnfapp/media/scripts')


def home(request):
    return render(request, 'mnfapp/index.html')


def dummyfilm(request):
    return render(request, 'mnfapp/preview_chamber.html')

def empty(request):
    return render(request, 'mnfapp/empty.html')
def newempty(request):
    return render(request, 'mnfapp/newempty.html')
def viewmore(request):
    return render(request, 'mnfapp/viewmore.html')     

def base(request):
    return render(request, 'mnfapp/base.html')
def mynarration(request):
    return render(request, 'mnfapp/mynarration.html')


# def members_home(request):
#     u = Uploads.objects.filter(user_uploaded=request.user)
#     context = {'obj': u}
#     return render(request, 'mnfapp/members_home.html', context)


# def narration(request):
#     return render(request, 'mnfapp/narration.html')


def script_saver(request):
    if request.method == "POST":
        if request.FILES['upload']:
            # print("coming")
            script_title = request.POST['script_title']
            author_name = request.POST['author_name']
            genre = request.POST['genre[]']
            script = request.FILES['upload']
            print(script.name)
            fs = FileSystemStorage()
            document_name = script.name
            filepath = os.path.join(settings.MEDIA_ROOT, document_name)
            if os.path.exists(filepath):
                os.remove(filepath)

            fs.save(document_name, script)

            s = Scripts(script_title=script_title, author_name=author_name,
                        genre=genre, document_name=document_name, script=script)
            s.save()
            # messages.success(
            #     request, "Thank you for uploading the script. You'll be notified once your video is ready")

            u = Uploads(uploaded_script=s, user_uploaded=request.user)
            u.save()
            print("saving")
            context = {
                'script_title': script_title,
                'author_name': author_name,
                'genre': genre,
                'script': script
            }
            if(script_title and author_name and genre and script):
                return render(request, 'mnfapp/base.html', context)
            return redirect('dummyfilm')


@login_required
def my_scripts(request):
    u = Uploads.objects.filter(user_uploaded=request.user)
    context = {'obj': u}
    return render(request, 'mnfapp/my_scripts.html', context)
