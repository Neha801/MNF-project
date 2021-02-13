from django.shortcuts import render

# Create your views here.
def conversion(request):
    return render(request, 'conversion/conversion.html')
