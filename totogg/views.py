from django.shortcuts import render
from .models import LCK_Data
from .models import rank
from .models import summerSummary
# from sklearn.metrics import log_loss, roc_auc_acore
import pandas as pd
import mlflow
import xgboost as xgb

# pip install pickle-mixin
from .models import recentSummary
from .models import gameSchedule
from datetime import datetime
import pandas as pd
# from .models import opggData
# Create your views here.
def totogg(request):
    data = rank.objects.all()
    schedules = gameSchedule.objects.all()
    t1s = []
    t2s = []
    for i in range(0, 2):
        s = schedules[i]
        t1s.append(s.team1)
        t2s.append(s.team2)
        date = s.date
    today = datetime.now().date()
    return render(
        request,
        'totogg/home.html',
        {"datas":data,
        't1s':t1s,
        't2s':t2s,
        'date':date,
        'today':today}
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

def ml_deply(request):

    # 정 어려우면 csv 파일로 받아서 team 만 전처리
    file = 'datas/pred_test.csv'
    data = pd.read_csv(file)

	# 'runs:/실험실행ID/model정보폴더명'
    # logged_model = 'runs:/e722aa6db7ba4ebfb0790f31e5d82bae/xgb_model'
    # 예측값
    # loaded_model = mlflow.pyfunc.load_model(logged_model)

    # pickle 파일 저장
    import pickle
    with open("./models/xgb_model.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    
    pred = loaded_model.predict(data)

    # 예측확률
    predb = loaded_model.predict_proba(data)
    # predb = loaded_model.predict_distribution(data)
    predicts = {"predict":pred, "preba":predb}

    
    return render (request, 'totogg/test.html', {'predicts':predicts})
    
def pred_data():
    #data = recentSummary.objects.all()
    schedules = gameSchedule.objects.all()
    t1s = []
    t2s = []
    t1_datas = []
    t2_datas = []
    chart_id = list(range(0, 10))
    schedule = []
    dates = []
    for i in range(0, 10):
        s = schedules[i]
        schedule.append(s)
        t1s.append(s.team1)
        t2s.append(s.team2)
        if s.date not in dates:
            dates.append(s.date)
    
    matches = []
    for date in dates:
        match_data = gameSchedule.objects.filter(date=date)
        g1t1 = match_data[0].team1
        g1t2 = match_data[0].team2
        g2t1 = match_data[1].team1
        g2t2 = match_data[1].team2
        matchs = {}
        matchs['date'] = date
        matchs['g1t1'] = g1t1
        matchs['g1t2'] = g1t2
        matchs['g2t1'] = g2t1
        matchs['g2t2'] = g2t2

        matches.append(matchs)


    zips = zip(t1s, t2s)
    for t1, t2 in zips:
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
    
    chid = [[0,1], [2,3], [4,5], [6,7], [8,9]]
    gs = zip(schedule, chart_id)
    gs1 = zip(matches, chid)
    return gs, gs1, t1_datas, t2_datas

def ml_deply(request):

    # 정 어려우면 csv 파일로 받아서 team 만 전처리
    # file = 'datas/pred_test.csv'
    # data = pd.read_csv(file)

	# 'runs:/실험실행ID/model정보폴더명'
    # logged_model = 'runs:/e722aa6db7ba4ebfb0790f31e5d82bae/xgb_model'
    # 예측값
    # loaded_model = mlflow.pyfunc.load_model(logged_model)

    gs, gs1, t1s, t2s = pred_data()

    predicts = []
    for t1, t2 in zip(t1s, t2s):
        predict = {}
        # pickle 파일 저장
        import pickle
        with open("./models/xgb_model_final.pkl", "rb") as f:
            loaded_model = pickle.load(f)
        
        gold = t1['gold']
        tot_dam = t1['tot_dam']
        kill = t1['kill']
        tower = t1['tower']
        inhibitor = t1['inhibitor']
        # herald = t1['herald']
        dragon = t1['dragon']
        # elder = t1['elder']
        baron = t1['baron']
        total_cs = t1['total_cs']
        df_temp1 = pd.DataFrame({"gold": [gold], "tot_dam": [tot_dam], "kill": [kill],\
        "tower": [tower], 'inhibitor': [inhibitor],'dragon': [dragon],\
        'baron': [baron], 'total_cs': [total_cs]})

        gold = t2['gold']
        tot_dam = t2['tot_dam']
        kill = t2['kill']
        tower = t2['tower']
        inhibitor = t2['inhibitor']
        # herald = t2['herald']
        dragon = t2['dragon']
        # elder = t2['elder']
        baron = t2['baron']
        total_cs = t2['total_cs']

        df_temp2 = pd.DataFrame({"gold": [gold], "tot_dam": [tot_dam], "kill": [kill],\
        "tower": [tower], 'inhibitor': [inhibitor],'dragon': [dragon],\
        'baron': [baron], 'total_cs': [total_cs]}) 
        
        # pred1 = loaded_model.predict(df_temp1)
        # pred2 = loaded_model.predict(df_temp2)

        # 예측확률
        predb1 = loaded_model.predict_proba(df_temp1)[0][1]
        predb2 = loaded_model.predict_proba(df_temp2)[0][1]
        sum = predb1 + predb2
        # predb = loaded_model.predict_distribution(data)
        # predict['predict1'] = pred1
        # predict['predict2'] = pred2
        predict['proba1'] = predb1 / sum * 100
        predict['proba2'] = predb2 / sum * 100
        predict['team1'] = t1['tname']
        predict['team2'] = t2['tname']
        
        predicts.append(predict)
        
    #return render (request, 'totogg/test.html', {'predicts':predicts})
    return predicts

def pred(request):
    gs, gs1, t1s, t2s = pred_data()
    pred = ml_deply(request)
    data_zip = zip(t1s, t2s, pred)
    return render(
        request,
        'totogg/pred.html',
        {"data_zips":data_zip,
        'gameSchedule': gs,
        'gameSchedule1': gs1,
        })



