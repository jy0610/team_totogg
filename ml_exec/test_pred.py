import mlflow
from numpy import int64
import pandas as pd
import pymysql

file = 'datas/pred_test.csv'
data = pd.read_csv(file)

gold = data['gold']
tot_dam = data['tot_dam']
kill = data['kill']
tower = data['tower']
inhibitor = data['inhibitor']
herald = data['herald']
dragon = data['dragon']
elder = data['elder']
baron = data['baron']
total_cs = data['total_cs']

if __name__ == '__main__':

	# 'runs:/실험실행ID/model정보폴더명'
    logged_model = 'runs:/050a9fbf0ef34703b6591daa225692b5/model'

    loaded_model = mlflow.pyfunc.load_model(logged_model)
    test_x = pd.DataFrame({"gold": [gold], "tot_dam": [tot_dam], "kill": [kill],\
        "tower": [tower], 'inhibitor': [inhibitor], 'herald': [herald], 'dragon': [dragon],\
        'elder': [elder], 'baron': [baron], 'total_cs': [total_cs]})

    test_x2 = test_x.astype(dtype='float64')

    # test_x = pd.DataFrame({"gold": [0.51], "tot_dam": [0.64], "kill": [0.3],\
    #     "tower": [0.3], 'inhibitor': [0.5], 'herald': [0.5], 'dragon': [0.3],\
    #     'elder': [0.0], 'baron': [0.0], 'total_cs': [0.52]})

    print(loaded_model.predict(test_x2))
    pred = loaded_model.predict(test_x2)
    # print(type(pred))
    
    # DB저장
    db = pymysql.connect(host='13.125.229.77',\
        port=3306, user='seok', passwd='wjdgotjr516',\
        db='pred_test', charset='utf8')

    pymysql.Binary(pred)

    pred_test = db.cursor()

    sql = '''
        INSERT INTO test VALUES (
            "'''  (pred);  '''"
        );
    '''

    pred_test.execute(sql)
    db.commit()
    db.close()
    print("DB 예측값 저장 완료")


