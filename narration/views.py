from django.shortcuts import render

# Create your views here.


def sampleNarrations(request):
    return render(request, 'narration/sampleNarrations.html')


def narrations(request):
    return render(request, 'narration/narrations.html')
def mynarrations(request):
    return render(request, 'narration/mynarrations.html')
