from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'index.html')

def photography(request):
    return render(request, 'photography.html')
