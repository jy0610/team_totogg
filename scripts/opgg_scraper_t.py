import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from slack_sdk import WebClient
from team.models import opggData
from webdriver_manager.chrome import ChromeDriverManager
import time

# SLACK_BOT_TOKEN = "xoxb-3643778575121-3631154727043-gWW2wAbXMEM2mNknCp9wivMW"
# slack_channel = "#slack-bot"

#chrome_options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1000,1000") # 윈도우 사이즈 결정
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument("headless") # 창을 띄우지않음
chrome_options.add_argument("--single-process")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.implicitly_wait(5)

url_pre = 'https://www.op.gg/summoners/kr/'

def slack_bot(message):
    print(message)
    requests.post("https://slack.com/api/chat.postMessage", 
        headers={"Authorization": "Bearer "+ SLACK_BOT_TOKEN}, 
        data={"channel": slack_channel, "text": message}
        )

#검색어
team = 'T1'
zeus = '자연계곡나무하늘'
oner = '0NER0'
faker = 'Hideonbush'
gumayusi = 'T1Gumayusi'
keria = '역천괴'
players = [zeus, oner, faker, gumayusi, keria]
pname = ['zeus', 'oner', 'faker', 'gumayusi', 'keria']

LCK = {'T1':{'team':team, 'players':players, 'pname':pname}}

# DRX
team = 'DRX'
kingen = 'kingen'
pyosik = 'DRXPyosik083O'
zeka = '베란다거북이'
deft = '베란다고양이'
beryl = '율자주세요'
players = [kingen, pyosik, zeka, deft, beryl]
pname = ['kingen', 'pyosik', 'zeka', 'deft', 'beryl']

LCK['DRX'] = {'team':team, 'players':players, 'pname':pname}

# 담원 기아
team = 'DK'
nuguri = '늘완벽하고싶다'
canyon = 'JUGKlNG'
showmaker = 'DKShowMaker'
deokdam = '아직은무겁다'
kellin = '참새크면비둘기'

players = [nuguri, canyon, showmaker, deokdam, kellin]
pname = ['nuguri', 'canyon', 'showmaker', 'deokdam', 'kellin']


LCK['DK'] = {'team':team, 'players':players, 'pname':pname}

# 젠지
team = 'GenG'
doran = '어리고싶다'
peanut = 'XiaoHuaSheng7'
chovy = '아파요머리가'
ruler = 'GenGRuler'
lehends = 'Lehends'

players = [doran, peanut, chovy, ruler, lehends]
pname = ['doran', 'peanut', 'chovy', 'ruler', 'lehends']

LCK['GenG'] = {'team':team, 'players':players, 'pname':pname}

# 리브 샌드박스
team = 'LSB'
dove = '비둘기도브'
croco = 'Croco'
clozer = '27haokan'
prince = '수피'
kael = '신입서폿'

players = [dove, croco, clozer, prince, kael]
pname = ['dove', 'croco', 'clozer', 'prince', 'kael']


LCK['LSB'] = {'team':team, 'players':players, 'pname':pname}

# 광동 프릭스
team = 'KDF'
kiin = '오뚜기3분미트볼'
ellim = '7I인'
fate = 'FATE'
teddy = 'teddy5'
hoit = '호잇이'

players = [kiin, ellim, fate, teddy, hoit]
pname = ['kiin', 'ellim', 'fate', 'teddy', 'hoit']


LCK['KDF'] = {'team':team, 'players':players, 'pname':pname}

# kt 롤스터
team = 'KT'
rascal = '리바이병장'
cuzz = '우찬굳'
aria = '오늘도잠에든다'
aiming = '강미나'
life = 'Rascal'

players = [rascal, cuzz, aria, aiming, life]
pname = ['rascal', 'cuzz', 'aria', 'aiming', 'life']


LCK['KT'] = {'team':team, 'players':players, 'pname':pname}

# 한화생명 e스포츠
team = 'HLE'
dudu = '따봉람머스'
onfleek = 'HLEOnFleek'
karis = 'HLEKaris1'
samd = 'HLESamD1' ###
vsta = '건들지마심기'

players = [dudu, onfleek, karis, samd, vsta]
pname = ['dudu', 'onfleek', 'karis', 'samd', 'vsta']


LCK['HLE'] = {'team':team, 'players':players, 'pname':pname}

# 프레딧 브리온
team = 'BRO'
morgan = 'BROMorgan'
umti = 'SeeuAG'
lava = '골목대장태훈이'
hena = 'BROHena'
delight = 'BRODelight'

players = [morgan, umti, lava, hena, delight]
pname = ['morgan', 'umti', 'lava', 'hena', 'delight']

LCK['BRO'] = {'team':team, 'players':players, 'pname':pname}

# 농심 레드포스
team = 'NS'
canna = 'Canna00'
dread = '오리지널찰떡쿠키'
bdd = '저사람뭔데에에에'
ghost = '농고심스트'
effort = '레전드오브롤1244'

players = [canna, dread, bdd, ghost, effort]
pname = ['canna', 'dread', 'bdd', 'ghost', 'effort']


LCK['NS'] = {'team':team, 'players':players, 'pname':pname}

def run():
  for key, value in LCK.items():
    tname = value['team']
    players = value['players']
    pnames = value['pname']

    #검색하려는 팀 명과 같은 데이터를 삭제처리
    opggData.objects.filter(teamName=tname).delete()

    for player, pname in zip(players, pnames):
      try:
        driver.get(url_pre + player)
        time.sleep(5)
        #items = driver.find_elements_by_css_selector("div.css-164r41r.e1r5v5160 li.css-1qq23jn.e1iiyghw3")
        items = driver.find_elements(By.CSS_SELECTOR, "div.css-164r41r.e1r5v5160 li.css-1qq23jn.e1iiyghw3")
        print("-"*20)
        for item in items:
          try:
            teamName = tname
            playerName = pname
            rst = item.find_element(By.CSS_SELECTOR, "div .game .result").text
            champ_img = item.find_element(By.CSS_SELECTOR, "div.info .champion img").get_attribute("src")
            champ = item.find_element(By.CSS_SELECTOR, "div .info  div .champion .icon a img").get_attribute("alt")
            kda = item.find_element(By.CSS_SELECTOR, "div .info  div .kda .k-d-a").text
            score = item.find_element(By.CSS_SELECTOR, "div .info  div .ratio span").text
            ka = item.find_element(By.CSS_SELECTOR, "div .info  div .stats .p-kill div").text[4:]
            cs = item.find_element(By.CSS_SELECTOR, "div .info  div .stats .cs div").text[3:6]
            g_time = item.find_element(By.CSS_SELECTOR, "div .game .length").text

            opggData(teamName=teamName, playerName=playerName, rst=rst, champ_img=champ_img, champ=champ, kda=kda, score=score, ka=ka, cs=cs, g_time=g_time).save()

            message = f"{teamName} - {playerName}\
                        결과 : {rst} \
                        챔피언 : {champ} \
                        kda : {kda} \
                        평점 : {score} \
                        킬관여 : {ka} \
                        CS : {cs} \
                        게임시간 : {g_time}"
            slack_bot(message)

          except Exception as e:
            print("--")
            continue

      except Exception as e:
          print("--")
          continue

  driver.quit()

#run()