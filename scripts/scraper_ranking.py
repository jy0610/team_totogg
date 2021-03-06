from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import requests
# from gamesaver.models import GameSaver
from selenium.webdriver.common.by import By
# from gamesaver.models import Rank
from datetime import datetime
import os 
from totogg.models import rank

# url
url = 'https://game.naver.com/esports/record/lck/team/lck_2022_summer'

# driver 설정과 지정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1000,1000") # 윈도우 사이즈 결정
chrome_options.add_argument("--headless") # 창을 띄우지않음
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--single-process")

chrome = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
chrome.implicitly_wait(5)

TEAM = []
score_n = []
logo_url = []
score_wins = []
score_loses = []
score_scd = []
score_wins_rates = []


def run():

    chrome.get(url)
    time.sleep(5)

    ranking_items = chrome.find_elements(By.CSS_SELECTOR, 'div.record_list_wrap__A8cnT')

    # print(ranking_items)

    for items in ranking_items:

        # team 정보 가져오기
        # teams = chrome.find_elements(By.CSS_SELECTOR, 'ul.record_list_team__2NtZO')
        teams = items.find_elements(By.CSS_SELECTOR, 'ul.record_list_team__2NtZO li.record_list_item__2fFsp')
    
        for team in teams:
            team_name = team.find_element(By.CSS_SELECTOR, 'span.record_list_name__27huQ').text
            # print(team_name)
            TEAM.append(team_name)
            # print(TEAM)

            # 순위
            rank_n = team.find_element(By.CSS_SELECTOR, 'span.record_list_rank__3mn_o').text

            score_n.append(rank_n)
            # print(score_n)

            # 팀로고
            logo = team.find_element(By.CSS_SELECTOR, 'span span.record_list_thumb_logo__1s1BT').get_attribute('style')
            logo = logo[23:].replace('");', '')
            # print(logo_url)
            logo_url.append(logo)

        # score 정보 가져오기
        score_datas = items.find_elements(By.CSS_SELECTOR, 'div.record_list_wrap_list__lkd3u > div > ul')
        
        for score_data in score_datas:
            # 승수 나타내기
            datas = score_data.find_elements(By.CSS_SELECTOR, 'li.record_list_item__2fFsp')

            for data in datas:
                wins = data.find_element(By.CSS_SELECTOR, 'span:nth-child(1)').text
                # print(wins) 
                score_wins.append(wins)
                
            # 패수 나타내기      
                roses = data.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
                # print(roses)
                score_loses.append(roses)

            # 득실차 나타내기
                scd = data.find_element(By.CSS_SELECTOR, 'span:nth-child(3)').text
                # print(scd)
                score_scd.append(scd)

            # 승률 나타내기
                win_rates = data.find_element(By.CSS_SELECTOR, 'span:nth-child(4)').text
                # print(win_rates)
                score_wins_rates.append(win_rates)

    # 확인
    # print(score_n)
    # print('='*100)
    # print(TEAM)
    # print('='*100)
    # print(score_wins)
    # print('='*100)
    # print(score_loses)
    # print('='*100)
    # print(score_scd)
    # print('='*100)
    # print(score_wins_rates)

    rank_data = []
    for a,b,c,d,e,f,g in zip(score_n, logo_url, TEAM, score_wins, score_loses, score_scd, score_wins_rates):
        data = []
        # rank_data.append(a,b,c,d,e)
        data.append(a)
        data.append(b)
        data.append(c)
        data.append(d)
        data.append(e)
        data.append(f)
        data.append(g)
        # data.append('\n')
        # print(rank_data)
        rank.objects.filter(team=c).delete()

        rank_data.append(data)

        # DB 저장
        rank(score_n=a,team_logo=b,team=c,score_wins=d,score_loses=e,score_scd=f,score_wins_rates=g).save()
        

    print(rank_data)
    print("script 실행")


    # 파일로 저장하기
    t = datetime.today().strftime("%Y-%m-%d-%H")

    base_path = './scraper_rank/'
    file_name = base_path + t + ".csv"
    
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    import csv
    with open(file_name, 'w', encoding='utf8', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rank_data)

    print("csv 파일 저장완료")

    
