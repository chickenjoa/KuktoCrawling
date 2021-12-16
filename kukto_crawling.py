#국토스크래핑
from os import sep
from pandas import DataFrame
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import math
import json
import numpy as np
import pandas as pd
import logging
def kukto():
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=AAAAAA1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
        options.add_experimental_option('prefs', prefs)
        URL = 'http://www.kiscon.net/gongsi/step_custom.asp'
        WD = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
        WD.get(URL)                                                   # 웹드라이버로 url open

        WD.implicitly_wait(0.1)
        # file = open("C:\\vscode\\data_text\\kukto_t.csv",'w')                 # 파일생성


        WD.implicitly_wait(0.1)

        # 체크박스
        task_dict = {'서울' : 'area2', '부산' : 'area3', '대구' : 'area4', '인천' : 'area5', '광주' : 'area6', '대전' : 'area7', '울산' : 'area8', '세종' : 'area9', '경기' : 'area10', '강원' : 'area11', '충북' : 'area12', '충남' : 'area13', '전북' : 'area14', '전남' : 'area15', '경북' : 'area16', '경남' : 'area17', '제주' : 'area18'}
        task_dict1 = {'토목건축공사업' : 'item1','토목공사업' : 'item2', '건축공사업' : 'item3', '조경공사업' : 'item4', '산업ㆍ환경설비공사업' : 'item5'}
        task_dict2 = {'가스시설시공업 제1종' : 'itemJun1', '가스시설시공업 제2종' : 'itemJun2', '가스시설시공업 제3종' : 'itemJun3', '강구조물공사업' : 'itemJun4', '건축물조립공사업' : 'itemJun5', '금속구조물ㆍ창호ㆍ온실공사업' : 'itemJun6', '기계설비공사업' : 'itemJun7', '난방시공업 제1종' : 'itemJun8', '난방시공업 제2종' : 'itemJun9', '난방시공업 제3종' : 'itemJun10',
        '도장공사업' : 'itemJun11', '미장ㆍ방수공사업' : 'itemJun12', '보링ㆍ그라우팅공사업' : 'itemJun13', '비계ㆍ구조물해체공사업' : 'itemJun14', '삭도설치공사업' : 'itemJun15', '상ㆍ하수도설비공사업' : 'itemJun16', '석공사업' : 'itemJun17', '수중공사업' : 'itemJun18', '습식ㆍ방수공사업' : 'itemJun19', '승강기설치공사업' : 'itemJun20',
        '시설물유지관리업' : 'itemJun21', '실내건축공사업' : 'itemJun22', '온실설치공사업' : 'itemJun23', '조경시설물설치공사업' : 'itemJun24', '조경식재공사업' : 'itemJun25', '조적공사업' : 'itemJun26', '준설공사업' : 'itemJun27', '지붕ㆍ판금공사업' : 'itemJun28', '지붕판금ㆍ건축물조립공사업' : 'itemJun29', '창호공사업' : 'itemJun30',
        '철강재설치공사업' : 'itemJun31', '철근ㆍ콘크리트공사업' : 'itemJun32', '철도ㆍ궤도공사업' : 'itemJun33', '철물공사업' : 'itemJun34', '토공사업' : 'itemJun35', '포장공사업' : 'itemJun36' }
        
        for task in task_dict.values():
            file = open("C:\\vscode\\data_text\\notest\\kukto_"+str(task)+".csv",'w',encoding='utf-8')
            num = 1
            for task2 in task_dict2.values():
                checkbox = WD.find_element_by_id(task)                                                      # 시도 체크박스
                checkbox.click()
                checkbox1 = WD.find_element_by_id(task2)                                                    # 종합공사업
                checkbox1.click()
                WD.implicitly_wait(0.1)
                WD.find_element_by_xpath('/html/body/form[1]/div[9]/div/div[2]/div/div[2]/a').click()       # 검색버튼
                WD.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                st_data = []
                getpaging(WD, st_data,file)
                WD.find_element_by_id('itemJun' + str(num)).click()
                num += 1

            
                                            
    except Exception as ex:
        logging.basicConfig(filename = "C:\\vscode\\data_text\\log\\debug.log", level=logging.DEBUG)
        logging.basicConfig(format='(%(asctime)s) %(levelname)s:%(message)s',
                    datefmt ='%m/%d %I:%M:%S %p',
                    level=logging.DEBUG)
        print('Error : ', ex)
    finally:
        # WD.quit()
        # file.close()
        end = time.time() - start                                       # 현재 시간 - 시작 시간 = 실행 시간
        print("총 실행 시간(초):", end)

def getpaging(WD, st_data, file):                                       # 메인페이지 크롤링
    obj = BeautifulSoup(WD.page_source, 'html.parser')              # new / BeautifulSoup 설정  
    pageCnt = obj.find("span", {"class", "org01 dml"}).find(text=True)
    pageCnt = int(pageCnt.replace(',', ''))                         # 추출한 전체 건수의 ',' 제거 후 정수형으로 변환
    pageCnt /= 5                                                    # 한 페이지 당 5건이 표시됨으로 5를 나눔(ex. 17.8)
    # pageCnt = pageCnt + (pageCnt * 0.1)
    pageCnt = math.ceil(pageCnt)                                    # 소수점 뒤의 자리 수 존재시 올림(ex. 18)
    print("Page Count :", pageCnt)
    cnt = 0
    isF = True
    while isF:
        obj = BeautifulSoup(WD.page_source, 'html.parser')          # new / BeautifulSoup 설정
        table = obj.find("table", {"summary": "검색결과"})
        for row in table.findAll("tr"):                             # 메인페이지 테이블 td요소들을 if문으로 조건을 걸어
            st_data = []                                            # td 요소를 하나씩 뽑아내는 소스입니다.
            cells = row.findAll("td")                               # st_data를 리스트형으로 초기화 합니다.                                                         
            WD.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            if len(cells) == 9:                                     # td 요소를 st_data에 각각 append시킵니다.
                id = cells[0].find(id="checklist01")
                st_data.append(id.get('value'))
                borough = cells[5].find(text=True)                  #업체상태
                st_data.append(borough.strip())
                amount = cells[7].find(text=True)                   #전화번호
                st_data.append(amount.strip())
                getDetail(WD, id.get('value'), st_data)             #상세페이지로 이동후 데이터 저장
                st_data.append("\n")    
                file.write('\t'.join(st_data))
                print('\t'.join(st_data))                      
                cnt += 1
        if pageCnt > 1:
            pageCnt -= 1
            WD.find_element_by_xpath('//a[@title="다음페이지로"]').click()
            WD.implicitly_wait(0.1)
        else:
            isF = False
        # break

def getDetail(WD, ncrEpNum, st_data):                                   # 상세페이지 크롤링
    WD.execute_script("send(\'" + ncrEpNum + "\');")                    # 상세페이지  이동
    
    WD.implicitly_wait(0.1)
    
    obj = BeautifulSoup(WD.page_source, 'html.parser')                  # new / BeautifulSoup 설정
    table = obj.find("table", {"summary": "일반현황"})                   #상세페이지에 들어와서 크롤링 하려는 소스입니다.
    
    row_total = len(table.findAll("tr"))
    row_index = 0
    variable_row = []
    variable_cell = []

    for rows in table.findAll("tr"):
        if(row_index == 1 or row_index == row_total - 1):
            for cells in rows.findAll("td"):
                st_data.append(cells.find(text=True).strip())

        if((row_total - 2) > row_index > 2):
            for cells in rows.findAll("td"):
                variable_cell.append(cells.find(text=True).strip())
            
            variable_row.append(variable_cell.copy())
            variable_cell.clear()

        row_index += 1
    
    
    # table1_rows = obj.select("table[summary=공사실적] > tbody > tr")
    # row_total = len(table1_rows)
    # row_index = 0

    # for rows in table1_rows:
    #     if(row_index < (row_total - 1)):
    #         for cells in rows.findAll("td"):
    #             st_data.append(cells.find(text=True).strip())

    #     row_index +=  1

    # table2 = obj.find("table", {"summary": "기술능력"})
    # for rows in table2.findAll("tr"):
    #     for cells in rows.findAll("td"):
    #         st_data.append(cells.find(text=True).strip())

    
    # table3 = obj.find("table", {"summary": "신용·재무정보"})     

    # row_index = 0
    # for rows in table3.findAll("tr"):   
    #     if(row_index < 3):  
    #         for cells in rows.findAll("td"):
    #             st_data.append(cells.find(text=True).strip())

    #     row_index +=  1

    for row in variable_row:
        for cell in row:
            st_data.append(cell)

    variable_row.clear()

    WD.back()
    
    WD.implicitly_wait(0.1)


    

# 메인 프로그램으로서 실행
if __name__ == '__main__':
    start = time.time() # 시작 시간
    kukto()