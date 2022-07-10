from django.shortcuts import render
from .models import LCK_Data
from .models import rank
from .models import summerSummary
from .models import recentSummary
# from .models import opggData
# Create your views here.
def totogg(request):
    data = rank.objects.all()
    return render(
        request,
        'totogg/home.html',
        {"datas":data}
        )

def chart(request):
    data = summerSummary.objects.all()
    return render(
        request,
        'totogg/chart.html',
        {"datas":data}
        )

def rank_page(request):
    data = rank.objects.all()
    return render(
        request,
        'totogg/rank.html',
        {"datas":data}
        )

def pred(request):
    data = recentSummary.objects.all()
    return render(
        request,
        'totogg/pred.html',
        {"datas":data}
        )
