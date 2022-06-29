from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import requests
from gamesaver.models import GameSaver
from selenium.webdriver.common.by import By
import discord
from discord.ext import commands

# # url
opgg_url = 'https://www.op.gg/summoners/kr/'

# T1
LCK = []
team = 'T1'
zeus = 'T1Zeus'
oner = '0NER0'
faker = 'Hideonbush'
gumayusi = 'T1Gumayusi'
keria = '역천괴'
players = [zeus, oner, faker, gumayusi, keria]
pname = ['zeus', 'oner', 'faker', 'gumayusi', 'keria']
T1 = [team, players, pname]
LCK.append(T1)

# DK
team = 'DK'
nuguri = '늘완벽하고싶다'
canyon = 'JUGKlNG'
showmaker = 'DKShowMaker'
deokdam = '아직은무겁다'
kellin = '참새크면비둘기'
players = [nuguri, canyon, showmaker, deokdam, kellin]
pname = ['nuguri', 'canyon', 'showmaker', 'deokdam', 'kellin']
DK = [team, players, pname]
LCK.append(DK)

# GenG
team = 'GenG'
doran = '어리고싶다'
peanut = 'XiaoHuaSheng7'
chovy = '아파요머리가'
ruler = 'GenGRuler'
lehends = 'Lehends'
players = [doran, peanut, chovy, ruler, lehends]
pname = ['doran', 'peanut', 'chovy', 'ruler', 'lehends']
GENG = [team, players, pname]
LCK.append(GENG)

# DRX
team = 'DRX'
kingen = 'kingen'
pyosik = 'DRXPyosik083O'
zeka = '베란다거북이'
deft = '베란다고양이'
beryl = '율자주세요'
players = [kingen, pyosik, zeka, deft, beryl]
pname = ['kingen', 'pyosik', 'zeka', 'deft', 'beryl']
DRX = [team, players, pname]
LCK.append(DRX)

# LSB
team = 'LSB'
dove = '비둘기도브'
croco = 'LSBCroc0'
clozer = '27haokan'
prince = '수피'
kael = '신입서폿'
players = [dove, croco, clozer, prince, kael]
pname = ['dove', 'croco', 'clozer', 'prince', 'kael']
LSB = [team, players, pname]
LCK.append(LSB)

# 광동 프릭스
team = 'KDF'
kiin = '오뚜기3분미트볼'
ellim = '7I인'
fate = 'FATE'
teddy = 'teddy5'
hoit = '호잇이'
players = [kiin, ellim, fate, teddy, hoit]
pname = ['kiin', 'ellim', 'fate', 'teddy', 'hoit']
KDF = [team, players, pname]
LCK.append(KDF)

# kt 롤스터
team = 'KT'
rascal = '리바이병장'
cuzz = 'Cuzz'
aria = '오늘도잠에든다'
aiming = '강미나'
life = 'Rascal'
players = [rascal, cuzz, aria, aiming, life]
pname = ['rascal', 'cuzz', 'aria', 'aiming', 'life']
KT = [team, players, pname]
LCK.append(KT)

# 한화생명 e스포츠
team = 'HLE'
dudu = '따봉람머스'
onfleek = 'HLEOnFleek'
karis = 'HLEKaris1'
samd = 'HLESamD1'
vsta = 'Vsta1'
players = [dudu, onfleek, karis, samd, vsta]
pname = ['dudu', 'onfleek', 'karis', 'samd', 'vsta']
HLE = [team, players, pname]
LCK.append(HLE)

# 프레딧 브리온
team = 'BRO'
morgan = 'BROMorgan'
umti = 'SeeuAG'
lava = '골목대장태훈이'
hena = 'BROHena'
delight = 'BRODelight'
players = [morgan, umti, lava, hena, delight]
pname = ['morgan', 'umti', 'lava', 'hena', 'delight']
BRO = [team, players, pname]
LCK.append(BRO)

# 농심 레드포스
team = 'NS'
canna = 'Canna00'
dread = '오리지널찰떡쿠키'
bdd = '저사람뭔데에에에'
ghost = 'DWGGhost'
effort = '레전드오브롤1244'
players = [canna, dread, bdd, ghost, effort]
pname = ['canna', 'dread', 'bdd', 'ghost', 'effort']
NS = [team, players, pname]
LCK.append(NS)

# driver 설정과 지정
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000") # 윈도우 사이즈 결정
# options.add_argument("headless") # 창을 띄우지않음
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
chrome.implicitly_wait(10)

# 슬랙
SLACK_TOKEN = 'xoxb-3092638135718-3616430141383-ddZhWZ7KOPidJTePkTxx84al'
slack_channel = '#test'

# slack 봇 만들기 https://developerdk.tistory.com/96
def slack_bot(message):
   #  print(message)
    requests.post("https://slack.com/api/chat.postMessage", 
        headers={"Authorization": "Bearer "+ SLACK_TOKEN}, 
        data={"channel": slack_channel, "text": message}
        )

# 디스코드
DISCORD_TOKEN = 'OTkxMjY2MzQ2NTUxNzUwNzE2.Gtv4W9.cDrChBqukjuAEh149awqoayhunKNIcKn5RJkTs'

def run():
 
   for teeam in LCK:
      # print('팀별 정보 : ',teeam)
      # print('선수 닉네임 : ',teeam[1])
      # print('선수 명 : ', teeam[2])
      tname = teeam[0]
      player = teeam[1]
      pnames = teeam[2]

      # DB 팀명이 같은 데이터 삭제
      # GameSaver.objects.all().delete()
      # GameSaver.objects.filter(teamName = team).delete()
      for player, pname in zip(players, pnames):
         
         chrome.get(opgg_url + player)
         time.sleep(5)

         # 전적갱신
         search = chrome.find_element(By.CSS_SELECTOR, "#content-header > div.css-rfknps.eioz3425 > div > div.header-profile-info > div.info > div.buttons > button.css-4e9tnt.eapd0am1")
         if search.get_attribute("disabled") == False:
            search.click()

         try : 

            # rst = chrome.find_elements(By.CSS_SELECTOR, "#content-container > div.css-150oaqg.e1shm8tx0 > div.css-164r41r.e1r5v5160 > li:nth-child(1) > div > div.game > div.result").text
            # print(player, rst)

            #  데이터 가져오기
            opgg_items = chrome.find_elements(By.CSS_SELECTOR, "div li.css-1qq23jn.e1iiyghw3")
            # for item in opgg_items:
            #    print(item)

            for item in opgg_items:

               teamName = tname
               # name = item.find_element(By.CSS_SELECTOR, "div.info .team span.name #text")
               rst = item.find_element(By.CSS_SELECTOR, "div.game .result").text
               img = item.find_element(By.CSS_SELECTOR, "div.info .champion img").get_attribute("src")
               champ = item.find_element(By.CSS_SELECTOR, "div.info .champion img").get_attribute("alt")
               kda = item.find_element(By.CSS_SELECTOR, "div.kda .k-d-a").text
               ratio = item.find_element(By.CSS_SELECTOR, "div.ratio span").text
               pkill = item.find_element(By.CSS_SELECTOR, "div.p-kill").text[3:]
               cs = item.find_element(By.CSS_SELECTOR, "div.cs").text[3:]
               gtime = item.find_element(By.CSS_SELECTOR, "div.game .length").text
               # print(player, '--', teamName, img, rst)
         
               message = f"{teamName} - {pname}\
                  \t결과 : {rst}\
                  \t게임시간 : {gtime}\
                  \t챔피언 : {champ}\
                  \tKDA : {kda}\
                  \t평점 : {ratio}\
                  \t킬관여율 : {pkill}\
                  \tcs 수급(분당cs) : {cs}"

               print(message)
               # slack_bot(message)

               GameSaver(teamName = team, name = player, rst = rst, img_url = img, champ = champ, kda = kda, ratio = ratio, pkill = pkill, cs = cs, gtime = gtime).save()

         except Exception as e:
               print("공백")
               pass    












  