from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import requests
from gamesaver.models import GameSaver
from selenium.webdriver.common.by import By

# # url
opgg_url = 'https://www.op.gg/summoners/kr/'

# 선수 닉네임
team = 'T1'
zeus = 'T1Zeus'
oner = '0NER0'
faker = 'Hideonbush'
gumayusi = 'T1Gumayusi'
keria = '역천괴'
players = [zeus, oner, faker, gumayusi, keria]

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

def run():
   # DB 팀명이 같은 데이터 삭제
   # GameSaver.objects.all().delete()
   # GameSaver.objects.filter(teamName = team).delete()

   for player in players:

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
            
            teamName = team
            player = player
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
      
            message = f"{teamName} - {player} \
               \t결과 : {rst}\
               \t게임시간 : {gtime}\
               \t챔피언 : {champ}\
               \tKDA : {kda}\
               \t평점 : {ratio}\
               \t킬관여율 : {pkill}\
               \tcs 수급(분당cs) : {cs}"

            print(message)
            # slack_bot(message)

            # GameSaver(teamName = team, name = player, rst = rst, img_url = img, champ = champ, kda = kda, ratio = ratio, pkill = pkill, cs = cs, gtime = gtime).save()

      except Exception as e:
            print("공백")
            pass    












  