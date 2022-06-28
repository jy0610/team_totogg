import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from opgg.models import opggData
from webdriver_manager.chrome import ChromeDriverManager

springUrl = 'https://qwer.gg/ko/leagues/LCK/2022/Spring?tournament=%22890%22'
# url -> '결과' 선택
# 2022 Spring 선택

# getRegular() -> Regular 선택 후 driver 반환
def getRegular(url, chrome_options):
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
  driver.get(url)
  driver.find_element_by_css_selector("button#headlessui-tabs-tab-10").click()
  #2022Spring 클릭
  driver.find_element_by_css_selector("div#headlessui-menu-button-14").click()
  driver.find_element_by_css_selector('[href^=/ko/leagues/LCK/2022/Spring]').click()
  #정규시즌 클릭
  driver.find_element_by_css_selector("button#headlessui-tabs-tab-16").click()
  driver.find_element_by_css_selector("div#headlessui-menu-item-304").click()

  return driver
  

# getPlayoff() -> playoff 선택 후 driver 반환
# scrapVic(TeamName)
# scrapDef(TeamName)



def run():
  chrome_options = webdriver.ChromeOptions()
  #chrome_options.add_argument("window-size=1000,1000") # 윈도우 사이즈 결정
  #chrome_options.add_argument("headless") # 창을 띄우지않음
  #chrome_options.add_argument("--single-process")
  #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  #chrome_options.add_argument('no-sandbox')
  #chrome_options.add_argument('--disable-dev-shm-usage')
  #검색하려는 팀 명과 같은 데이터를 삭제처리
  driver = getRegular(springUrl, chrome_options)
  items = driver.find_elements_by_css_selector("li.mt-1.first:mt-0")
  for item in items:
    item.click()

# for문 두 번: 정규시즌 + 플레이오프
# for문 :
# 매치 바 선택 -> Match Detail 선택
# 세트 선택 -> 1세트부터
# 이긴 팀 스크래핑 함수
# 진 팀 스크래핑 함수
# 데미지, 시야점수는 선수별 데이터를 합쳐서 입력

