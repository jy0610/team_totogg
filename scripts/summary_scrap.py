from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from totogg.models import summerSummary
from webdriver_manager.chrome import ChromeDriverManager
import time


sum_url = 'https://qwer.gg/ko/leagues/LCK/2022/Summer?tournament=%22949%22'

def deleteSideBar(driver):
  #x_button = driver.find_elements_by_css_selector("div#__next div div.flex.h-12 button.h-b-8 svg.fill-gray-400")
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div:nth-child(1) > div").click()
  driver.find_element(By.CSS_SELECTOR, "#__next > div:nth-child(1) > div.px-b-6.mt-px.hidden.h-11.select-none.items-center.justify-between.bg-gray-800.lg\:flex > div.flex.w-56.items-center.justify-end > div").click()



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
  driver.get(sum_url)
  #time.sleep(5)
  print("--")

  #사이드바 제거
  deleteSideBar(driver)

  #팀 통계 클릭
  driver.find_element(By.CSS_SELECTOR, "button#headlessui-tabs-tab-13").click()
  print("Clicked!")
  time.sleep(1)

  #팀명 클릭
  driver.find_element(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > thead > tr > th.h-26px.select-none.whitespace-nowrap.px-1.py-1.text-xs.font-normal.cursor-pointer.text-left.capitalize").click()
  print("Sorted!")
  time.sleep(1)
  
  tnames = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(2) > a > div > div.transition-colors.group-hover\:text-red-500")

  #int 변환할 것
  rates = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td.py-4.px-1.text-xs.text-center.font-roboto.text-gray-500")
  
  kills = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(7)")

  golds = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(8)")

  barons = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(9)")

  dragons = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(10)")

  towers = driver.find_elements(By.CSS_SELECTOR, "div.min-h-10.relative.overflow-x-auto.overflow-hidden.rounded-md.mt-2 > table > tbody > tr > td:nth-child(11)")

  for tname, rate, kill, gold, baron, dragon, tower in zip(tnames, rates, kills, golds, barons, dragons, towers):
    tn = tname.text
    r = float(rate.text.replace("%",""))
    k = float(kill.text)
    g = int(gold.text.replace(",",""))
    b = float(baron.text)
    d = float(dragon.text)
    t = float(tower.text)
    
    summerSummary.objects.filter(tname=tn).delete()
    summerSummary(tname=tn, rate=r, kill=k, gold=g, baron=b, dragon=d, tower=t).save()
    print(tn, " data saved!")