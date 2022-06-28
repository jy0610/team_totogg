import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from slack_sdk import WebClient
from team.models import opggData
from selenium.webdriver.common.by import By


SLACK_BOT_TOKEN = "xoxb-3084686717031-3656409265063-wulPAfUjwU3NKD62K2ysPmzF"
slack_channel = "#opgg"
def slack_bot(message):
    print(message)
    requests.post("https://slack.com/api/chat.postMessage", 
        headers={"Authorization": "Bearer "+ SLACK_BOT_TOKEN}, 
        data={"channel": slack_channel, "text": message}
        )
def getDriver(name):
  options = webdriver.ChromeOptions()
  options.add_argument("headless")
  url_pre = 'https://www.op.gg/summoners/kr/'
  url = url_pre + name
  path = "C:\gitdoc\team_totogg\scripts\chromedriver.exe"
  driver = webdriver.Chrome(path, options=options)
  driver.get(url)
  driver.implicitly_wait(5)
  return driver
def run(team, players):
  #검색하려는 팀 명과 같은 데이터를 삭제처리
  opggData.objects.filter(teamName=team).delete()
  for player in players:
    try:
      driver = getDriver(player)
      items = driver.find_elements_by_css_selector("div.css-164r41r.e1r5v5160 li.css-1qq23jn.e1iiyghw3")
      print("-"*20)
      for item in items:
        try:
          teamName = team
          playerName = player
          # name = item.find_element(By.CSS_SELECTOR, "div.info .team span.name #text")
          rst = item.find_element(By.CSS_SELECTOR, "div.game .result").text
          champ_img = item.find_element(By.CSS_SELECTOR, "div.info .champion img").get_attribute("src")
          champ = item.find_element(By.CSS_SELECTOR, "div.info .champion img").get_attribute("alt")
          kda = item.find_element(By.CSS_SELECTOR, "div.kda .k-d-a").text
          score = item.find_element(By.CSS_SELECTOR, "div.ratio span").text
          ka = item.find_element(By.CSS_SELECTOR, "div.p-kill").text[3:]
          cs = item.find_element(By.CSS_SELECTOR, "div.cs").text[3:]
          g_time = item.find_element(By.CSS_SELECTOR, "div.game .length").text
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
        
      driver.quit()
    except Exception as e:
        print("--")
        continue
team = 'T1'
zeus = 'T1Zeus'
oner = '0NER0'
faker = 'Hideonbush'
gumayusi = 'T1Gumayusi'
keria = '역천괴'
players = [zeus, oner, faker, gumayusi, keria]
run(team, players)