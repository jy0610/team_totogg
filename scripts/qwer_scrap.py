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
  #x_button = driver.find_elements_by_css_selector("div#__next div div.flex.h-12 button.h-b-8 svg.fill-gray-400")
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div:nth-child(1) > div").click()
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div.flex.w-56.items-center.justify-end > div").click()
  #for x in x_button:
  #  x.click()

# getPlayoff() -> playoff 선택 후 driver 반환
# scrapBlue(TeamName)
#def scrapBlue(team):

# scrapRed(TeamName)



def run():
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("window-size=1100,1000") # 윈도우 사이즈 결정
  #chrome_options.add_argument("headless") # 창을 띄우지않음
  #chrome_options.add_argument("--single-process")
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
    #detail = driver.find_element(By.CSS_SELECTOR, "a['href']")
    detail = driver.find_element(By.XPATH, "//a[contains(@href, '/ko/matches/')]")
    #/ko/matches/
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
    try:
      #refresh
      driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div > div div.container.transition-all div:nth-child(3) div.flex.items-center.justify-between.lg\:mt-2 div").click()
      print("refreshed")
      
      driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all border-red-500 bg-red-500 hover:bg-red-400 active:bg-red-600 h-10 px-3 py-2 text-base')]").click()
      print("done click")

      gtime = driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div div div.container.transition-all div:nth-child(3) div.mt-3 div div:nth-child(1) div.flex.items-center.justify-between.px-2.py-1.lg\:px-4 div.mr-4.flex.flex-1.items-center.text-xs div")
      print(gtime.text)
      gold = driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div div div.container.transition-all div:nth-child(3) div.mt-3 div div:nth-child(1) div.h-13.hidden.items-center.justify-between.space-x-24.border-t.border-gray-900.px-4.lg\:flex > div.flex.items-center.space-x-3.lg\:space-x-4.flex-1 > span:nth-child(2)")
      print(gold.text)

      time.sleep(5)
      b = driver.find_element(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all > div:nth-child(3) > div.mt-3 > div > div.border-t.border-gray-900 > div.scrollbar-hide.overflow-x-auto.whitespace-nowrap.p-2.md\:p-4 button span")
      b.click()
      print("done click")
      time.sleep(5)
      t = driver.find_element(By.CSS_SELECTOR, "#headlessui-tabs-panel-15 ul li:nth-child(1) div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md table tbody tr:nth-child(1) td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell div")
      print(t.text)
      teams = driver.find_element(By.CSS_SELECTOR, "#headlessui-tabs-panel-15 > ul > li:nth-child(1) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center > div.ml-2.font-bold")
      print(teams.text)

      
      #teams = driver.find_elements(By.XPATH, "//div[contains(@class, 'ml-2 font-bold')]")

      # t = driver.find_elements(By.CSS_SELECTOR, "div.mt-3::before")
      # print(t)
      
      #teams = driver.find_elements(By.CSS_SELECTOR, "div.ml-2.font-bold")
      #teams = driver.find_element(By.CSS_SELECTOR, "div.py-4 li.mt-4 div.flex div.font-axiforma")
      #teams = driver.find_elements(By.CSS_SELECTOR, "ul > li:nth-child(1) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center")

      #result = driver.find_elements(By.XPATH, "//strong[contains(@class, 'ml-3 text-')]")
      #side = driver.find_elements(By.XPATH, "//span[contains(@class, 'pt-0.5 font-bold')]")
      #print(teams[0].find_element(By.CSS_SELECTOR, "div.ml-2.font-bold").text)
      # for x in teams:
      #   print(type(x))
      #   print(x)
      #   time.sleep(1)
      

    except Exception as e:
      print("예외발생")
      print(e)

    while True:
      pass
    #print(result)
    #print(side)

    
    

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

