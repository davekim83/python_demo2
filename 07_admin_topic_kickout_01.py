# 토픽 내보내기 테스트
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
by_selector = driver.find_element_by_css_selector  # 자주쓰는 스크립트를 간소화 하기
driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(5)  # 암묵적 대기 Global
# 로그인 하기
user_id = "dave.kim@tosslab.com"
user_pw = "@Worud1209"
by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').clear()  # 이메일 입력창 내용 비우기
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').send_keys(user_id)  # Email ID 입력
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys(user_pw)  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)
by_xpath('//*[@id="wrap"]/article/div/section[2]/article/ul/li[3]/div/button[2]/span/span').click()  # Dave Test.Team 으로 진입 (li[n] 숫자를 각 계정에 맞게 설정해야 함

# 자주 사용하는 요소의 XPath 값 저장해두기
m_input = by_xpath('//*[@id="message_input"]')  # 메시지 입력창을 "m_input" 변수에 저장

# 토픽 생성하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/i').click()  # 토픽 추가 메뉴 [+] 더보기 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/span').click()  # 새로운 토픽 생성하기 클릭
time.sleep(1)
by_xpath('//*[@id="topic-create-name"]').send_keys(title)  # 토픽 이름 입력
by_xpath('//*[@id="create_new_channel"]').click()  # 생성하기 클릭
time.sleep(2)

# 멤버 초대하기
by_xpath('//*[@id="msgs_container"]/div[2]/div/div[3]/button').click()  # 멤버 초대하기 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 멤버 선택 최상단 한명씩
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[2]/button[2]').click()  # 초대하기 클릭
time.sleep(0.5)

# 토픽 멤버 내보내기 1
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/a').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(1)
# 토픽 멤버 내보내기 2
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/a').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(1)
# 토픽 멤버 내보내기 3
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/a').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(1)
m_input.send_keys('모든 멤버를 쫒아냈습니다!! *^^* ' + Keys.ENTER)
print('모든 멤버를 쫒아냈습니다!! *^^*')
m_input.send_keys('테스트가 완료 되어 브라우저를 종료 합니다.' + Keys.ENTER)
print('멤버 내보내기 테스트가 완료 되었습니다.')
time.sleep(3)

driver.quit()
