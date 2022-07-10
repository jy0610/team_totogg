from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.model_selection import train_test_split
#---------------------------------------------
import collections
from sklearn import preprocessing
#---------------------------------------------
from sklearn import tree
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier, plot_importance

#---------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns # heatmap
import pandas as pd
import numpy as np
import numpy as np
from pandas.io.json import json_normalize
import warnings

# Import mlflow
from sklearn.metrics import f1_score
import mlflow
import mlflow.sklearn
import xgboost as xgb
import mlflow.xgboost


# mlflow.xgboost.autolog()
# mlflow.sklearn.autolog()

# 데이터 불러오기
# load Data
file = 'datas/LCK_2022_Spring_v2.csv'
data = pd.read_csv(file)

# label encoding(rst, side)
le = preprocessing.LabelEncoder()

data['rst'] = le.fit_transform(data['rst']) # 승리시 1, 패배시 0

# gold tot_dam kill death assist total_cs는 경기마다 큰 차이를 보이기에 퍼센트로 대체
# gold 전처리
for i in range(220):
    even_gold = data['gold'][2 * i]
    odd_gold = data['gold'][2 * i + 1]
    odd_gold_data = odd_gold/(odd_gold+even_gold)
    even_gold_data = even_gold/(odd_gold+even_gold)
    data['gold'][2 * i] = even_gold_data
    data['gold'][2 * i + 1] = odd_gold_data

#tot_dam 전처리
for i in range(220):
    even_dam = data['tot_dam'][2 * i]
    odd_dam = data['tot_dam'][2 * i + 1]
    odd_dam_data = odd_dam/(odd_dam+even_dam)
    even_dam_data = even_dam/(odd_dam+even_dam)
    data['tot_dam'][2 * i] = even_dam_data
    data['tot_dam'][2 * i + 1] = odd_dam_data

# kill 전처리
for i in range(220):
    even_kill = data['kill'][2 * i]
    odd_kill = data['kill'][2 * i + 1]
    odd_kill_data = odd_kill/(odd_kill+even_kill)
    even_kill_data = even_kill/(odd_kill+even_kill)
    data['kill'][2 * i] = even_kill_data
    data['kill'][2 * i + 1] = odd_kill_data
    
# death 전처리
for i in range(220):
    even_death = data['death'][2 * i]
    odd_death = data['death'][2 * i + 1]
    odd_death_data = odd_death/(odd_death+even_death)
    even_death_data = even_death/(odd_death+even_death)
    data['death'][2 * i] = odd_death_data
    data['death'][2 * i + 1] = even_death_data
    
# assist 전처리
for i in range(220):
    even_assist = data['assist'][2 * i]
    odd_assist = data['assist'][2 * i + 1]
    even_assist_data = even_assist/(odd_assist+even_assist)
    odd_assist_data = odd_assist/(odd_assist+even_assist)
    data['assist'][2 * i] = even_assist_data
    data['assist'][2 * i + 1] = odd_assist_data

# total_cs 전처리
for i in range(220):
    even_total_cs = data['total_cs'][2 * i]
    odd_total_cs = data['total_cs'][2 * i + 1]
    even_total_cs_data = even_total_cs/(odd_total_cs+even_total_cs)
    odd_total_cs_data = odd_total_cs/(odd_total_cs+even_total_cs)
    data['total_cs'][2 * i] = even_total_cs_data
    data['total_cs'][2 * i + 1] = odd_total_cs_data

# 오브젝트의 경우 숫자가 거의 정해져있기에 최대값으로 나눔
# 오브젝트 전처리
data['inhibitor'] = data['inhibitor']/5
data['herald'] = data['herald']/2
data['dragon'] = data['dragon']/6
data['baron'] = data['baron']/3
data['tower'] = data['tower']/11

data = data.drop(['gtime', 'id', 'match_num', 'side', 'sight', 'team', 'set'], axis=1)

#상관관계 히트맵
heatmap_data = data[['rst', 'gold', 'tot_dam', 'kill', 'death', 'assist', 'tower',
                     'inhibitor', 'herald', 'dragon',  'elder', 'baron', 'total_cs']]

colormap = plt.cm.BuGn
plt.figure(figsize=(10, 8))
plt.title("spring data(corr)", y = 1.05, size = 15)
sns.heatmap(heatmap_data.astype(float).corr(), linewidths = 0.1, vmax = 1.0,
           square = True, cmap = colormap, linecolor = "white", annot = True, annot_kws = {"size" : 10})

#XGBoost
train_x = np.array(pd.DataFrame(data, columns=['gold', 'tot_dam', 'kill', 'tower', 'inhibitor', 'herald', 'dragon',  'elder', 'baron', 'total_cs']))  
train_y = np.array(pd.DataFrame(data, columns=['rst'])) 

def evaluation(model, test_x, test_y):
    pred_y = model.predict(test_x)
    score = f1_score(test_y, pred_y, average='weighted')
    return score

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    mlflow.set_experiment('gg00_xgb')
    with mlflow.start_run() as run:

        # split data
        X = train_x
        y = train_y
        X_train, X_test, Y_train, Y_test = train_test_split(train_x, train_y, test_size=0.20, random_state=48)

        xgb_model = xgb.XGBClassifier(base_score=0.5, booster='gbtree',
                                colsample_bylevel=1, colsample_bynode=1,
                                colsample_bytree=1, gamma=0, gpu_id=-1,
                                importance_type='gain',
                                interaction_constraints='',
                                learning_rate=1, max_delta_step=0,
                                max_depth=4, min_child_weight=1, monotone_constraints='()',
                                n_estimators=300, n_jobs=48,
                                num_parallel_tree=1, random_state=0,
                                reg_alpha=0, reg_lambda=1,
                                scale_pos_weight=1, subsample=1,
                                tree_method='exact', validate_parameters=1,
                                verbosity=None)
        evals = [(X_test,Y_test)]

        # xgb_model.get_params(deep = True).get_params

        xgb_model.fit(X_train, Y_train, early_stopping_rounds = 100, eval_metric='logloss', eval_set = evals, verbose=True)
        import pickle
        pickle.dump(xgb_model, open('./models/xgb_model.pkl', 'wb'))
        y_pred = xgb_model.predict(X_test)
        # proba = xgb_model.predict_proba(X_test)[:,1]
        score = evaluation(xgb_model, X_test, Y_test)

        mlflow.log_param("y_pred", y_pred)
        mlflow.log_metric("f1 score", score)
        mlflow.log_param("train", file)
        mlflow.log_param("train num", len(X_train))
        # mlflow.log_param("proba", proba)
        
        # mlflow.log_param("class", collections.Counter(train_y))
        # mlflow.log_param("class num", len(set(Y_train)))
        mlflow.log_artifact(file)
        mlflow.sklearn.log_model(xgb_model, "xgb_model")

        acc = accuracy_score(Y_test,y_pred)
        print("정확도 : ",accuracy_score(Y_test,y_pred))
        # mlflow.log_metric("accuracy_score", acc)

        conf_mat = confusion_matrix(Y_test,y_pred)
        print(confusion_matrix(Y_test,y_pred))
        # mlflow.log_metric("confusion", conf_mat)