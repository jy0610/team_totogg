from django.shortcuts import render
from .models import LCK_Data
# from .models import opggData
# Create your views here.
def totogg(request):
  return render(request, 'totogg/home.html')

def pred(request):
  return render(request, 'totogg/pred.html')