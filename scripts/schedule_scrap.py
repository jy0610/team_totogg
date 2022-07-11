import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from totogg.models import gameSchedule
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta

url = 'https://qwer.gg/ko/schedules'
# url -> '결과' 선택
# 2022 Spring 선택

# getRegular() -> Regular 선택 후 driver 반환


def getSchedule(driver):
  #정규시즌 클릭
  driver.find_element(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > div > ul > li:nth-child(2) > div").click()
  time.sleep(1)

def deleteSideBar(driver):
  #x_button = driver.find_elements_by_css_selector("div#__next div div.flex.h-12 button.h-b-8 svg.fill-gray-400")
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div:nth-child(1) > div").click()
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div.flex.w-56.items-center.justify-end > div").click()

# getPlayoff() -> playoff 선택 후 driver 반환
# scrapBlue(TeamName)




def run():
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("window-size=1200,1000") # 윈도우 사이즈 결정
  #chrome_options.add_argument("headless") # 창을 띄우지않음
  #chrome_options.add_argument("--single-process")
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  #chrome_options.add_argument('no-sandbox')
  #chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
  driver.get(url)
  print("--")

  #사이드바 제거
  deleteSideBar(driver)
  getSchedule(driver)
  print('LCK Selected!')

  dates = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > h3")
  g1t1s = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(1) > a > div > div.font-axiforma.flex.flex-1.items-center.justify-end.space-x-2.text-xs.lg\:text-sm > strong")
  g1t2s = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(1) > a > div > div:nth-child(4) > strong")
  g2t1s = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(2) > a > div > div.font-axiforma.flex.flex-1.items-center.justify-end.space-x-2.text-xs.lg\:text-sm > strong")
  g2t2s = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(2) > a > div > div:nth-child(4) > strong")
  g1times = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(1) > a > div > div.flex.h-6.items-center.justify-center.overflow-hidden.rounded.text-center.font-bold.text-xs.lg\:h-8.lg\:text-base > div")
  g2times = driver.find_elements(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all.pb-8.pt-14 > ul > li > ul > li:nth-child(2) > a > div > div.flex.h-6.items-center.justify-center.overflow-hidden.rounded.text-center.font-bold.text-xs.lg\:h-8.lg\:text-base > div")
  
  for d, g1t1, g1t2, g2t1, g2t2, g1t, g2t in zip(dates, g1t1s, g1t2s, g2t1s, g2t2s, g1times, g2times):
    try:
      # 날짜, 시간 타입 변환
      datetime_format = "%Y년 %m월 %d일"
      date = datetime.strptime(d.text, datetime_format).date()
      g1time = g1t.text
      g2time = g2t.text
      # 지난 경기 삭제
      #gameSchedule.objects.filter(date__lte=datetime.now().date() - timedelta(days=3)).delete()
      gameSchedule.objects.filter(date__lte=datetime.now().date()).delete()
      if (gameSchedule.objects.filter(date=date).count() == 0):
        #gameSchedule.objects.filter(date <= datetime.today().date()).delete()

        # DB 입력
        gameSchedule(date=date, time=g1time, team1=g1t1.text, team2=g1t2.text, set=1).save()
        gameSchedule(date=date, time=g2time, team1=g2t1.text, team2=g2t2.text, set=2).save()

        #결과 출력
        print(date, " ", g1t1.text, " ", g1time, " ", g1t2.text)
        print(date, " ", g2t1.text, " ", g2time, " ", g2t2.text)

    except Exception as e:
      print("예외발생")
      print(e)
  
  

  
#run()



# for문 두 번: 정규시즌 + 플레이오프
# for문 :
# 매치 바 선택 -> Match Detail 선택
# 세트 선택 -> 1세트부터
# 이긴 팀 스크래핑 함수
# 진 팀 스크래핑 함수
# 데미지, 시야점수는 선수별 데이터를 합쳐서 입력

