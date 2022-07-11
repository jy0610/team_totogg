from django.shortcuts import render
from .models import LCK_Data
from .models import rank
from .models import summerSummary
from .models import recentSummary
from .models import gameSchedule
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
    #data = recentSummary.objects.all()
    schedule = gameSchedule.objects.all()
    t1s = []
    t2s = []
    t1_datas = []
    t2_datas = []
    # for s in schedule:
    #     t1s.append(s.team1)
    #     t2s.append(s.team2)
    for i in range(0, 10):
        s = schedule[i]
        t1s.append(s.team1)
        t2s.append(s.team2)
    
    tname_zip = zip(t1s, t2s)
    for t1, t2 in tname_zip:
        team1_data = recentSummary.objects.get(tname=t1)
        team2_data = recentSummary.objects.get(tname=t2)
        t1_data = {}
        t2_data = {}

        t1_data['tname'] = t1
        t2_data['tname'] = t2

        # gold 전처리
        t1g = team1_data.gold
        t2g = team2_data.gold
        sum_gold = t1g + t2g
        t1g = t1g / sum_gold
        t2g = t2g / sum_gold
        t1_data['gold'] = t1g
        t2_data['gold'] = t2g

        # damage 전처리
        t1d = team1_data.tot_dam
        t2d = team2_data.tot_dam
        sum_dam = t1d + t2d
        t1d = t1d / sum_dam
        t2d = t2d / sum_dam
        t1_data['tot_dam'] = t1d
        t2_data['tot_dam'] = t2d

        # kill 전처리
        t1k = team1_data.kill
        t2k = team2_data.kill
        sum_kill = t1k + t2k
        t1k = t1k / sum_kill
        t2k = t2k / sum_kill
        t1_data['kill'] = t1k
        t2_data['kill'] = t2k

        # tower 전처리
        t1t = team1_data.tower
        t2t = team2_data.tower
        t1t = t1t / 11
        t2t = t2t / 11
        t1_data['tower'] = t1t
        t2_data['tower'] = t2t

        # inhibitor 전처리
        t1i = team1_data.inhibitor
        t2i = team2_data.inhibitor
        t1i = t1i / 5
        t2i = t2i / 5
        t1_data['inhibitor'] = t1i
        t2_data['inhibitor'] = t2i

        # dragon 전처리
        t1d = team1_data.dragon
        t2d = team2_data.dragon
        t1d = t1d / 6
        t2d = t2d / 6
        t1_data['dragon'] = t1d
        t2_data['dragon'] = t2d

        # baron 전처리
        t1b = team1_data.baron
        t2b = team2_data.baron
        t1b = t1b / 3
        t2b = t2b / 3
        t1_data['baron'] = t1b
        t2_data['baron'] = t2b

        # cs 전처리
        t1cs = team1_data.total_cs
        t2cs = team2_data.total_cs
        sum_cs = t1cs + t2cs
        t1cs = t1cs / sum_cs
        t2cs = t2cs / sum_cs
        t1_data['total_cs'] = t1cs
        t2_data['total_cs'] = t2cs

        t1_datas.append(t1_data)
        t2_datas.append(t2_data)
    
    data_zip = zip(t1_datas, t2_datas)
    return render(
        request,
        'totogg/pred.html',
        {"data_zips":data_zip})
