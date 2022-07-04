from django.shortcuts import render
from .models import LCK_Data
import csv
import pandas as pd
from .models import rank
# from .models import opggData
# Create your views here.
def totogg(request):
    data = rank.objects.all()
    return render(
        request,
        'totogg/home.html',
        {"datas":data}
        )

def pred(request):
  return render(request, 'totogg/pred.html')

