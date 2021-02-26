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
from mnfapp.models import Uploads, Scripts, Uploadvideo,Uploadrefer,Uploaddo,Uploadlive,Uploadboundary
from django.template import RequestContext



BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR, 'mnfapp/static/mnfapp/media/scripts')


def home(request):
    return render(request, 'mnfapp/index.html')


def dummyfilm(request):
    return render(request, 'mnfapp/preview_chamber.html')

def name(request):
    if request.method == 'POST':
        if request.FILES.get('recordaudio'):
            recfile = request.FILES.get('recordaudio')
            fs = FileSystemStorage()
            file_name = recfile.name
            filepath = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(filepath):
                os.remove(filepath)
            fs.save(file_name, recfile)
            s=Uploadvideo(recfile=recfile)
            s.save()
            return render(request, 'mnfapp/name.html')
        else:
            name = request.POST.get('hala')
            s=Uploadvideo(name=name)
            s.save()
            return render(request, 'mnfapp/name.html')
    return render(request, 'mnfapp/name.html')
    

def live(request):
    if request.method == 'POST':
        if request.FILES.get('livingvideo'):
            livevideo = request.FILES.get('livingvideo')
            fs = FileSystemStorage()
            file_name = livevideo.name
            filepath = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(filepath):
                os.remove(filepath)
            fs.save(file_name, livevideo)
            s=Uploadlive(livevideo=livevideo)
            s.save()
            return render(request, 'mnfapp/live.html')
        else:
            livename = request.POST.get('livingname')
            s=Uploadlive(livename=livename)
            s.save()
            return render(request, 'mnfapp/live.html')
    return render(request, 'mnfapp/live.html')

def do(request):
    if request.method == 'POST':
        if request.FILES.get('donevideo'):
            dovideo = request.FILES.get('donevideo')
            fs = FileSystemStorage()
            file_name = dovideo.name
            filepath = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(filepath):
                os.remove(filepath)
            fs.save(file_name, dovideo)
            s=Uploaddo(dovideo=dovideo)
            s.save()
            return render(request, 'mnfapp/do.html')
        else:
            doname = request.POST.get('donename')
            s=Uploaddo(doname=doname)
            s.save()
            return render(request, 'mnfapp/do.html')
    return render(request, 'mnfapp/do.html')
def referred(request):
    if request.method == 'POST':
        if request.FILES.get('refer'):
            refervideo = request.FILES.get('refer')
            fs = FileSystemStorage()
            file_name = refervideo.name
            filepath = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(filepath):
                os.remove(filepath)
            fs.save(file_name, refervideo)
            s=Uploadrefer(refervideo=refervideo)
            s.save()
            return render(request, 'mnfapp/referred.html')
        else:
            refername = request.POST.get('referred')
            s=Uploadrefer(refername=refername)
            s.save()
            return render(request, 'mnfapp/referred.html')
    return render(request, 'mnfapp/referred.html')

def boundaryless(request):
    if request.method == 'POST':
        if request.FILES.get('boundarylesvideo'):
            boundaryvideo = request.FILES.get('boundarylesvideo')
            fs = FileSystemStorage()
            file_name = boundaryvideo.name
            filepath = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(filepath):
                os.remove(filepath)
            fs.save(file_name, boundaryvideo)
            s=Uploadboundary(boundaryvideo=boundaryvideo)
            s.save()
            return render(request, 'mnfapp/boundaryless.html')
        else:
            boundaryname = request.POST.get('boundarylesname')
            s=Uploadboundary(boundaryname=boundaryname)
            s.save()
            return render(request, 'mnfapp/boundaryless.html')
    return render(request, 'mnfapp/boundaryless.html')
def basket(request):
    return render(request, 'mnfapp/basket.html')
def special(request):
    return render(request, 'mnfapp/special.html')
def concern(request):
    return render(request, 'mnfapp/concern.html')

def showvideo(request):
   
    return render(request, 'mnfapp/showvideo.html')
 


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
