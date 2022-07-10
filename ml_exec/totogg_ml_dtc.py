# 머신러닝
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score, StratifiedKFold
from sklearn.model_selection import GridSearchCV

# mlflow
import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import warnings

# Import mlflow
import mlflow
import mlflow.sklearn


mlflow.sklearn.autolog()

# load Data
file = 'datas/LCK_2022_Spring_v2.csv'
lck_df = pd.read_csv(file)

lck_df = lck_df.drop('gtime', axis=1)

# label encoding(rst, side)
le = preprocessing.LabelEncoder()

lck_df['rst'] = le.fit_transform(lck_df['rst']) # 승리시 1, 패배시 0
lck_df['side'] = le.fit_transform(lck_df['side']) # red side 1, blue side 0
# lck_df.head(5)

# ohe(team) 동일한 수준
lck_team_ohe = pd.get_dummies(lck_df['team'])
lck_df_01 = pd.concat([lck_df, lck_team_ohe], axis=1)
lck_df_01 = lck_df_01.drop('team', axis=1)
lck_df_02 = lck_df_01.drop(['id', 'match_num', 'side','rst'], axis=1)

# 정규화하기 (gold, tot_dam, total_cs)
from sklearn.preprocessing import MinMaxScaler

standfeatures = ['gold', 'tot_dam', 'total_cs']
notstandfeatures = lck_df_02.columns.drop(standfeatures)
# feat = lck_df_02.columns.drop('rst')

# 칼럼 수를 맞추기 위해 target drop
df_lck = lck_df_02.drop(notstandfeatures, axis=1)
scaler = MinMaxScaler()

df_lck_scaler = scaler.fit_transform(df_lck)

# df 로 변환
feat = ['stand_gold','stand_tot_dam','stand_total_cs']
lckDF = pd.DataFrame(data=df_lck_scaler, columns=feat)
lckDF.head(3)

# 다시 target 추가
lckDF['target'] = lck_df.rst
# lckDF.head(3)

lck_df_03 = pd.concat([lck_df_02,lckDF], axis=1)
lck_df_03['match_num'] = lck_df.match_num
lck_df_03['side'] = lck_df_01.side

lck_df_111 = lck_df_03.drop(['gold','tot_dam','total_cs'], axis=1)

lck_df_04 = lck_df_111[['match_num', 'set', 'side',\
    'BRO', 'DK', 'DRX', 'GEN', 'HLE', 'KDF', 'KT', 'LSB', 'NS', 'T1',\
    'stand_gold', 'stand_tot_dam', 'kill', 'death', 'assist', 'tower', 'inhibitor',
    'herald', 'dragon', 'elder', 'baron', 'sight', 'stand_total_cs', 'target']]

lck_df_05 = lck_df_04[['side','stand_gold', 'stand_tot_dam', 'kill', 'death', 'assist', 'tower', 'inhibitor',
    'herald', 'dragon', 'elder', 'baron', 'sight', 'stand_total_cs', 'target']]


if __name__ == "__main__":

    # 실험실 지정
    warnings.filterwarnings("ignore")
    mlflow.set_experiment('gg01')
    
    # split data
    X = lck_df_04.iloc[:, :-1]
    y = lck_df_04.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 , train_size=0.7, random_state=42)

    model_dtc = DecisionTreeClassifier()
    model_dtc.fit(X_train, y_train)
    y_pred = model_dtc.predict(X_test)

    mlflow.sklearn.log_model(model_dtc, "model_dtc")

    print(classification_report(y_test, y_pred))