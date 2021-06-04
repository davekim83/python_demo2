# 할 일 테스트
# Author : Dave

import time
import random
import string
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


# 랜덤 토픽 타이틀 생성
n = 10
rand_str = ""
for i in range(n):
    rand_str += str(random.choice(string.ascii_uppercase + string.digits))
title = rand_str
print(title)

driver = Chrome()  # 사용하는 디바이스의 OS 별로 지정한 PATH의 chromedriver 를 실행 할 수 있도록 환경변수 선언
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
by_selector = driver.find_element_by_css_selector
driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(5)  # 암묵적 대기 Global

# Default Setting
# 멤버의 권한에 따라 Elements 의 속성이 다르기 때문에 멤버 권한에 따라 일부 스크립트를 수정해야 함
# 관리자 이상 = div[7],[8] / 정회원 = div[6],[7]

# 잔디 랜딩 접속 > 로그인
by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').clear()  # 이메일 입력창 내용 비우기
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').send_keys('dave.kim@tosslab.com')  # Email ID 입력
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys('@Worud1209')  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)
by_xpath('//*[@id="wrap"]/article/div/section[2]/article/ul/li[3]/div/button[2]/span/span').click()  # Dave Test.Team 으로 진입 (li[n] 숫자를 각 계정에 맞게 설정해야 함

# 자주 사용하는 요소의 XPath 값 저장해두기
m_input = by_xpath('//*[@id="message_input"]')  # 메시지 입력창을 "m_input" 변수에 저장
print('할 일 테스트를 시작합니다.')
time.sleep(1)

# 보드 뷰 토픽으로 점프
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[2]/div/button').click()  # Jump 메뉴 클릭
by_xpath('//*[@id="quick-launcher-filter"]').send_keys('보드뷰입니다')  # 검색할 토픽명 입력
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(Keys.ENTER)  # Enter 키 사용하여 검색한 토픽으로 진입
time.sleep(1)
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[1]').click()  # [+] 업로드 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/ul/li[2]/a/i').click()  # 할 일 클릭(툴 메뉴)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/section[1]/button').click()  # 할 일 생성 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]/div/dl[1]/dd/div[1]/div').text



