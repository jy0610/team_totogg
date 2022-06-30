import requests
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from opgg.models import opggData
from webdriver_manager.chrome import ChromeDriverManager
import time

springUrl = 'https://qwer.gg/ko/leagues/LCK/2022/Spring?tournament=%22890%22'
# url -> '결과' 선택
# 2022 Spring 선택

# getRegular() -> Regular 선택 후 driver 반환

def getSpring(driver):
  #2022Spring 클릭
  driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all flex w-full items-center justify-between text-xs border-gray-600 hover:bg-gray-600 active:bg-opacity-75 h-10 px-3 py-2 text-base')]").send_keys(Keys.ENTER)

  driver.find_element(By.XPATH, "//a[contains(@href, '/ko/leagues/LCK/2022/Spring')]").send_keys(Keys.ENTER)

def getRegular(driver):
  #정규시즌 클릭
  driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all text-xs border-gray-600 hover:bg-gray-600 active:bg-opacity-75 h-10 px-3 py-2 text-base')]").send_keys(Keys.ENTER)

  reg = driver.find_elements(By.XPATH, "//div[contains(@id, 'headlessui-menu-item-')]")
  reg[0].click()

def getPlayoff(driver):
  #정규시즌 클릭
  driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all text-xs border-gray-600 hover:bg-gray-600 active:bg-opacity-75 h-10 px-3 py-2 text-base')]").send_keys(Keys.ENTER)
  reg = driver.find_elements(By.XPATH, "//div[contains(@id, 'headlessui-menu-item-')]")
  reg[1].click()

def deleteSideBar(driver):
  x_button = driver.find_elements_by_css_selector("div#__next div div.flex.h-12 button.h-b-8 svg.fill-gray-400")
  for x in x_button:
    x.click()

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
  #time.sleep(5)
  print("--")

  #사이드바 제거
  deleteSideBar(driver)
  
  #경기 결과 클릭
  driver.find_element_by_css_selector("button#headlessui-tabs-tab-10").click()
  
  #2022 Spring 정규시즌 선택
  getSpring(driver)
  getRegular(driver)
  #getPlayoff(driver)
  
  #items = driver.find_elements_by_css_selector("li.mt-1.first:mt-0")
  items = driver.find_elements(By.XPATH, "//button[contains(@id, 'headlessui-disclosure-button-')]")

  for item in items:
    #마지막에 driver.back() 넣어서 뒤로가기
    item.click()
    #url에서 match번호 가져오기! -> 한 번 스크랩 한 경기는 스크랩 하지 않음
    # 매치 번호, 팀 명으로 Delete 여부 결정
    detail = driver.find_element(By.XPATH, "//a[contains(@href, '/ko/matches/')]")
    match_link = detail.get_attribute("href")
    #item.click()
    #detail.click()
    
    #아이디어
    #링크를 찾는 메소드 -> 링크를 리스트에 저장 -> for문 돌려서 스크랩 하기
    #item.click()로 열고 마지막에 item.click()로 닫기
    #driver(link) deleteSideBar()


  # 세트 구분하는 기능
  # 매치, 세트를 DB에 넣을 예정
  
  

  #-----
  # Blue, Red 식별
    driver.get(match_link)
    deleteSideBar(driver)

    teams = driver.find_elements(By.XPATH, "//div[contains(@class, 'ml-2 font-bold')]")
    result = driver.find_elements(By.XPATH, "//strong[contains(@class, 'ml-3 text-')]")
    side = driver.find_elements(By.XPATH, "//span[contains(@class, 'pt-0.5 font-bold')]")

    print(teams)
    print(result)
    print(side)

    while True:
      pass
    

    #DB 저장
    #print()
    #driver.back()
    #back 이후에 경기 결과 클릭 해줄 것!
  
  

  
#run()



# for문 두 번: 정규시즌 + 플레이오프
# for문 :
# 매치 바 선택 -> Match Detail 선택
# 세트 선택 -> 1세트부터
# 이긴 팀 스크래핑 함수
# 진 팀 스크래핑 함수
# 데미지, 시야점수는 선수별 데이터를 합쳐서 입력

