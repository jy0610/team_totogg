def pred_data():
    #data = recentSummary.objects.all()
    schedule = gameSchedule.objects.all()
    t1s = []
    t2s = []
    sets = []
    t1_datas = []
    t2_datas = []
    # for s in schedule:
    #     t1s.append(s.team1)
    #     t2s.append(s.team2)
    for i in range(0, 10):
        s = schedule[i]
        t1s.append(s.team1)
        t2s.append(s.team2)
        sets.append(s.set)
    
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
    
    recent_10games = {'team1_datas': t1_datas, 'team2_datas':t2_datas, 'sets' : sets}
    game_pd =  pd.DataFrame(recent_10games)
    # ml_deply(recent_10games)
    return game_pd

def pred(request):
    return render(
        request,
        'totogg/pred.html')
        
def ml_deply(request):

    # 정 어려우면 csv 파일로 받아서 team 만 전처리
    # file = 'datas/pred_test.csv'
    # data = pd.read_csv(file)

	# 'runs:/실험실행ID/model정보폴더명'
    # logged_model = 'runs:/e722aa6db7ba4ebfb0790f31e5d82bae/xgb_model'
    # 예측값
    # loaded_model = mlflow.pyfunc.load_model(logged_model)

    print(pred_data())
    datas = pred_data()
    print(type(datas))

    # for key, value in datas:
    #     print()
    


    # # 예측할 데이터
    # gold = datas['gold']
    # tot_dam = datas['tot_dam']
    # kill = datas['kill']
    # tower = datas['tower']
    # inhibitor = datas['inhibitor']
    # herald = datas['herald']
    # dragon = datas['dragon']
    # elder = datas['elder']
    # baron = datas['baron']
    # total_cs = datas['total_cs']

    # pred_pd = pd.DataFrame({"gold": [gold], "tot_dam": [tot_dam], "kill": [kill],\
    #     "tower": [tower], 'inhibitor': [inhibitor], 'herald': [herald], 'dragon': [dragon],\
    #     'elder': [elder], 'baron': [baron], 'total_cs': [total_cs]})

    # pickle 파일 저장
    # import pickle
    # with open("./models/xgb_model.pkl", "rb") as f:
    #     loaded_model = pickle.load(f)
    
    # pred = loaded_model.predict(pred_pd)

    # # 예측확률
    # predb = loaded_model.predict_proba(pred_pd)
    # # predb = loaded_model.predict_distribution(data)
    # predicts = {"predict":pred, "preba":predb, "team1":team1, "team2":team2}

    
    # return render (request, 'totogg/pred.html', {'predicts':predicts})