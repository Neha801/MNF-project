from django.shortcuts import render

# Create your views here.


def chamber(request):
    return render(request, 'chamber/chamber.html')


# def dummyfilm(request):
#     return render(request, 'chamber/chamber.html')
