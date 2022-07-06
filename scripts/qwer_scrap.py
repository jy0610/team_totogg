import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from totogg.models import LCK_Data
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
  time.sleep(1)
  reg = driver.find_elements(By.XPATH, "//div[contains(@id, 'headlessui-menu-item-')]")
  reg[0].click()

def getPlayoff(driver):
  #정규시즌 클릭
  driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all text-xs border-gray-600 hover:bg-gray-600 active:bg-opacity-75 h-10 px-3 py-2 text-base')]").send_keys(Keys.ENTER)
  time.sleep(1)
  reg = driver.find_elements(By.XPATH, "//div[contains(@id, 'headlessui-menu-item-')]")
  reg[1].click()

def deleteSideBar(driver):
  #x_button = driver.find_elements_by_css_selector("div#__next div div.flex.h-12 button.h-b-8 svg.fill-gray-400")
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div:nth-child(1) > div").click()
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div.flex.w-56.items-center.justify-end > div").click()

# getPlayoff() -> playoff 선택 후 driver 반환
# scrapBlue(TeamName)
def scrapBlue(driver, match_num, set):
  #게임 시간
  gtime = driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div div div.container.transition-all div:nth-child(3) div.mt-3 div div:nth-child(1) div.flex.items-center.justify-between.px-2.py-1.lg\:px-4 div.mr-4.flex.flex-1.items-center.text-xs div").text
  print("게임 시간 : ", gtime)

  #골드
  gold = int(driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div div div.container.transition-all div:nth-child(3) div.mt-3 div div:nth-child(1) div.h-13.hidden.items-center.justify-between.space-x-24.border-t.border-gray-900.px-4.lg\:flex > div.flex.items-center.space-x-3.lg\:space-x-4.flex-1 > span:nth-child(2)").text.replace(",",""))
  print("총 골드 : ", gold)
  
  #데미지 추출
  top_dam = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  jg_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(1) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  mid_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(1) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  ad_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(1) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  spt_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(1) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  tot_dam = int(top_dam) + int(jg_dam) + int(mid_dam) + int(ad_dam) + int(spt_dam)
  print('총 데미지 : ', tot_dam)

  #팀명 추출
  team = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center > div.ml-2.font-bold").text
  rst = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center > strong").text
  side = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.flex.items-center.space-x-2.capitalize > div > span").text
  print("팀 명 : ", team)
  print("결과 : ", rst)
  print("진영 : ", side)

  #K/D/A
  kda = driver.find_element(By.CSS_SELECTOR, "div.h-13.hidden.items-center.justify-between.space-x-24.border-t.border-gray-900.px-4.lg\:flex > div:nth-child(1) > span.font-axiforma.text-sm.text-gray-100").text.strip().split("/")
  kill = int(kda[0])
  death = int(kda[1])
  assist = int(kda[2])
  print("KDA : ", kill, "/", death, "/", assist)

  #Object
  tower = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(1) > div").text)
  inhibitor = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(2) > div").text)
  herald = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(3) > div").text)
  dragon = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(4) > div").text)
  elder = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(5) > div").text)
  baron = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div:nth-child(1) > div.mt-3.xl\:mt-0 > ul > li:nth-child(6) > div").text)
  
  #시야점수
  t_sight = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td:nth-child(7) > div").text[:2])
  j_sight = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td:nth-child(7) > div").text[:2])
  m_sight = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td:nth-child(7) > div").text[:2])
  a_sight = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td:nth-child(7) > div").text[:2])
  s_sight = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td:nth-child(7) > div").text[:2])
  sight = t_sight + j_sight + m_sight + a_sight + s_sight

  #CS
  t_cs = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td:nth-child(8) > div").text[:3])
  j_cs = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td:nth-child(8) > div").text[:3])
  m_cs = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td:nth-child(8) > div").text[:3])
  a_cs = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td:nth-child(8) > div").text[:3])
  s_cs = int(driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td:nth-child(8) > div").text[:3])
  total_cs = t_cs + j_cs + m_cs + a_cs + s_cs

  #DB에 입력
  LCK_Data(match_num=match_num, team=team, rst=rst, side=side, gtime=gtime,
          gold=gold, tot_dam=tot_dam, kill=kill, death=death, assist=assist,
          tower=tower, inhibitor=inhibitor, herald=herald, dragon=dragon,
          elder=elder, baron=baron, sight=sight, total_cs=total_cs, set=set).save()


def scrapRed(driver, match_num, set):
  #게임 시간
  gtime = driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div div div.container.transition-all div:nth-child(3) div.mt-3 div div:nth-child(1) div.flex.items-center.justify-between.px-2.py-1.lg\:px-4 div.mr-4.flex.flex-1.items-center.text-xs div").text
  print("게임 시간 : ", gtime)

  #골드
  gold = int(driver.find_element(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all > div:nth-child(3) > div.mt-3 > div > div:nth-child(1) > div.h-13.hidden.items-center.justify-between.space-x-24.border-t.border-gray-900.px-4.lg\:flex > div.flex.items-center.space-x-3.lg\:space-x-4.flex-1 > span:nth-child(4)").text.replace(",",""))
  print("총 골드 : ", gold)
  
  #데미지 추출
  top_dam = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  jg_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  mid_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  ad_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  spt_dam = driver.find_element(By.CSS_SELECTOR,"ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td.py-4.px-1.text-xs.text-center.py-0.pt-3.xl\:w-52.hidden.lg\:table-cell > div").text.replace(',','')
  tot_dam = int(top_dam) + int(jg_dam) + int(mid_dam) + int(ad_dam) + int(spt_dam)
  print('총 데미지 : ', tot_dam)

  #팀명 추출
  team = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center > div.ml-2.font-bold").text
  rst = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.font-axiforma.flex.items-center > strong").text
  side = driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.flex.items-center.justify-between.px-4.text-sm.text-gray-100 > div.flex.items-center.space-x-2.capitalize > div > span").text
  print("팀 명 : ", team)
  print("결과 : ", rst)
  print("진영 : ", side)

  #K/D/A
  kda = driver.find_element(By.CSS_SELECTOR, "div.h-13.hidden.items-center.justify-between.space-x-24.border-t.border-gray-900.px-4.lg\:flex > div:nth-child(3) > span.font-axiforma.text-sm.text-gray-100").text.strip().split("/")
  kill = int(kda[0])
  death = int(kda[1])
  assist = int(kda[2])
  print("KDA : ", kill, "/", death, "/", assist)

  #Object
  tower = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(1) > div").text)
  inhibitor = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(2) > div").text)
  herald = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(3) > div").text)
  dragon = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(4) > div").text)
  elder = int(driver.find_element(By.CSS_SELECTOR, " div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(5) > div").text)
  baron = int(driver.find_element(By.CSS_SELECTOR, "div.flex.content-between.justify-between.border-t.border-gray-900.p-3.lg\:p-4.xl\:flex-row > div.flex.flex-1.flex-col.sm\:flex-row.sm\:items-center.sm\:space-x-5.items-end.sm\:flex-row-reverse.sm\:space-x-reverse > div.mt-3.xl\:mt-0.text-right > ul > li:nth-child(6) > div").text)
  
  #시야점수
  t_sight = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td:nth-child(7) > div").text[:2])
  j_sight = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td:nth-child(7) > div").text[:2])
  m_sight = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td:nth-child(7) > div").text[:2])
  a_sight = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td:nth-child(7) > div").text[:2])
  s_sight = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td:nth-child(7) > div").text[:2])
  sight = t_sight + j_sight + m_sight + a_sight + s_sight

  #CS
  t_cs = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(1) > td:nth-child(8) > div").text[:3])
  j_cs = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(2) > td:nth-child(8) > div").text[:3])
  m_cs = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(3) > td:nth-child(8) > div").text[:3])
  a_cs = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(4) > td:nth-child(8) > div").text[:3])
  s_cs = int(driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md > table > tbody > tr:nth-child(5) > td:nth-child(8) > div").text[:3])
  total_cs = t_cs + j_cs + m_cs + a_cs + s_cs

  #DB에 입력
  LCK_Data(match_num=match_num, team=team, rst=rst, side=side, gtime=gtime,
          gold=gold, tot_dam=tot_dam, kill=kill, death=death, assist=assist,
          tower=tower, inhibitor=inhibitor, herald=herald, dragon=dragon,
          elder=elder, baron=baron, sight=sight, total_cs=total_cs, set=set).save()



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
  driver.find_element(By.CSS_SELECTOR, "button#headlessui-tabs-tab-10").click()
  
  #매치 링크를 저장하는 리스트
  links = []
  #매치 넘버를 저장하는 리스트
  match_nums = []
  
  #2022 Spring 정규시즌 선택
  getSpring(driver)
  getRegular(driver)
  print('Regular Season Selected!')
  time.sleep(1)
  items = driver.find_elements(By.XPATH, "//button[contains(@id, 'headlessui-disclosure-button-')]")
  for item in items:
    item.click()
    time.sleep(1)
    detail = driver.find_element(By.XPATH, "//a[contains(@href, '/ko/matches/')]")
    match_link = detail.get_attribute("href")
    match_num = match_link.split("/")[5]
    links.append(match_link)
    match_nums.append(match_num)
    item.click()
  
  #2022 Spring PlayOff 선택
  getPlayoff(driver)
  print('PlayOffs Selected!')
  time.sleep(1)
  items = driver.find_elements(By.XPATH, "//button[contains(@id, 'headlessui-disclosure-button-')]")
  for item in items:
    item.click()
    time.sleep(1)
    detail = driver.find_element(By.XPATH, "//a[contains(@href, '/ko/matches/')]")
    match_link = detail.get_attribute("href")
    match_num = match_link.split("/")[5]
    links.append(match_link)
    match_nums.append(match_num)
    item.click()
    print('Saved!')
  

  #-----
  # Blue, Red 식별
  for match_link, match_num in zip(links, match_nums):  
    # url에서 match번호 가져오기! -> 한 번 스크랩 한 경기는 스크랩 하지 않음
    # or
    # 매치 번호, 팀 명으로 Delete 여부 결정
    LCK_Data.objects.filter(match_num=match_num).delete()

    driver.get(match_link)
    time.sleep(1)
    deleteSideBar(driver)
    time.sleep(1)
    try:
      #refresh
      driver.find_element(By.CSS_SELECTOR, "#__next div.min-h-content div > div div.container.transition-all div:nth-child(3) div.flex.items-center.justify-between.lg\:mt-2 div").click()
      print("refreshed")

      #select set
      sets = driver.find_elements(By.XPATH, "//li[@class='shrink-0']//button[contains(@class, 'select-none rounded border text-center outline-none transition-all border')]")
      sn = 1
      for set in sets:
        set.click()
      #driver.find_element(By.XPATH, "//button[contains(@class, 'select-none rounded border text-center outline-none transition-all border-red-500 bg-red-500 hover:bg-red-400 active:bg-red-600 h-10 px-3 py-2 text-base')]").click()
        print(sn, " Set Selected!")
        sn += 1
        time.sleep(1)

        #요약 클릭
        b = driver.find_element(By.CSS_SELECTOR, "#__next > div.min-h-content > div > div > div.container.transition-all > div:nth-child(3) > div.mt-3 > div > div.border-t.border-gray-900 > div.scrollbar-hide.overflow-x-auto.whitespace-nowrap.p-2.md\:p-4 button span")
        b.click()
        print("Summary Selected!")
        time.sleep(1)

        print("-"*20)
        scrapBlue(driver, match_num, sn)
        print("-"*20)
        scrapRed(driver, match_num, sn)
        print("-"*20)


    #DB 입력:
    
      

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

