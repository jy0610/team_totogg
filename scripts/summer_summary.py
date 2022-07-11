from matplotlib.pyplot import bar
from totogg.models import Summer_Data, recentSummary

def run():
  # 데이터 불러오기
  datas = Summer_Data.objects.values()
  
  # 팀 이름 가져오기
  tn = []
  for data in datas:
    tname = data['team']
    if tname not in tn:
      tn.append(tname)
  # reverse=True -> 정렬 반대로
  tnames = sorted(tn, key=str.lower)
  
  # 팀명으로 for문 돌리기
  # 팀별 전적 가져오기
  # 데이터별 평균 구하기
  for tname in tnames:
    t_datas = Summer_Data.objects.values().filter(team=tname)
    # 최근 10개 데이터로만 for문 돌리기
    gold = 0.0
    dam = 0.0
    kill = 0.0
    tower = 0.0
    inhibitor = 0.0
    dragon = 0.0
    baron = 0.0
    cs = 0.0
    for i in range(0, 10):
      t_data = t_datas[i]
      #데이터 저장
      gold += float(t_data['gold'])
      dam += float(t_data['tot_dam'])
      kill += float(t_data['kill'])
      tower += float(t_data['tower'])
      inhibitor += float(t_data['inhibitor'])
      dragon += float(t_data['dragon'])
      baron += float(t_data['baron'])
      cs += float(t_data['total_cs'])
    
    #평균
    gold = gold / 10
    dam = dam / 10
    kill = kill / 10
    tower = tower / 10
    inhibitor = inhibitor / 10
    dragon = dragon / 10
    baron = baron / 10
    cs = cs / 10

    # 해당 팀의 통계 삭제
    recentSummary.objects.filter(tname=tname).delete()

    # DB에 저장
    recentSummary(tname=tname, gold=gold, dam=dam, kill=kill, tower=tower, inhibitor=inhibitor, dragon=dragon, baron=baron, cs=cs).save()

    #print(type(t_datas))

  # for data in datas:
  #   print(data.kill)