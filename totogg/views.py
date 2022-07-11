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
    
def pred(request):
    data = recentSummary.objects.all()
    return render(
        request,
        'totogg/pred.html',
        {"datas":data}
        )
