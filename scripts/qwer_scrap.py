import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from opgg.models import opggData
from webdriver_manager.chrome import ChromeDriverManager
import time

springUrl = 'https://qwer.gg/ko/leagues/LCK/2022/Spring?tournament=%22890%22'
# url -> '결과' 선택
# 2022 Spring 선택

# getRegular() -> Regular 선택 후 driver 반환
def getRegular(driver):
  #driver.find_element_by_css_selector("button#headlessui-tabs-tab-10").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-tabs-tab-10')]").send_keys(Keys.ENTER) 
  #2022Spring 클릭
  #driver.find_element_by_css_selector("div#headlessui-menu-button-14").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, "//div[contains(@id, 'headlessui-menu-button-14')]").send_keys(Keys.ENTER)
  #driver.find_element_by_css_selector('[href^=/ko/leagues/LCK/2022/Spring]').send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, "//a[contains(@href, '/ko/leagues/LCK/2022/Spring')]").send_keys(Keys.ENTER)
  #정규시즌 클릭
  #driver.find_element_by_css_selector("button#headlessui-tabs-tab-16").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-tabs-tab-16')]").send_keys(Keys.ENTER)
  #driver.find_element_by_css_selector("div#headlessui-menu-item-304").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH, "//div[contains(@id, 'headlessui-menu-item-304')]").send_keys(Keys.ENTER)


# getPlayoff() -> playoff 선택 후 driver 반환
# scrapBlue(TeamName)
#def scrapBlue(team):

# scrapRed(TeamName)



def run():
  chrome_options = webdriver.ChromeOptions()
  #chrome_options.add_argument("window-size=1000,1000") # 윈도우 사이즈 결정
  #chrome_options.add_argument("headless") # 창을 띄우지않음
  #chrome_options.add_argument("--single-process")
  #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  #chrome_options.add_argument('no-sandbox')
  #chrome_options.add_argument('--disable-dev-shm-usage')
  #검색하려는 팀 명과 같은 데이터를 삭제처리
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
  driver.get(springUrl)
  time.sleep(5)
  print("--")


   #사이드바 제거(임시)
  driver.find_element_by_css_selector("div.-ml-3 svg").click()
  time.sleep(5)
  print("--")

  driver.find_element_by_css_selector("div.-mr-3 svg").click()
  time.sleep(5)


  print("--")
  print(driver.find_element_by_css_selector("button#headlessui-tabs-tab-10"))
  print("--")
  driver.find_element_by_css_selector("button#headlessui-tabs-tab-10").click()
  print("--")
  #driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-tabs-tab-10')]").click()
  

  # while(True):
  #   pass
  
  #getRegular(driver)
  # items = driver.find_elements_by_css_selector("li.mt-1.first:mt-0")
  # for item in items:
  #   item.send_keys(Keys.ENTER)
  #   driver.find_element_by_css_selector("div.flex.cursor-pointer.items-center").send_keys(Keys.ENTER)

    #세트 구분하는 기능

    # -----
    #Blue, Red 식별
    # teams = driver.find_elements_by_css_selector("li.mt-4.first:mt=0 div.ml-2.font-bold").text
    # result = driver.find_elements_by_css_selector("li.mt-4.first:mt=0 strong.ml-3.text-green-500").text
    # side = driver.find_elements_by_css_selector("li.mt-4.first:mt=0 div div span.pt-0.5").text

    # print(side)

  
#run()



# for문 두 번: 정규시즌 + 플레이오프
# for문 :
# 매치 바 선택 -> Match Detail 선택
# 세트 선택 -> 1세트부터
# 이긴 팀 스크래핑 함수
# 진 팀 스크래핑 함수
# 데미지, 시야점수는 선수별 데이터를 합쳐서 입력

