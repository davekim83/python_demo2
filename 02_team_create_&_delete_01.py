# 팀 생성 & 삭제 테스트
# Author : Dave

import time
import random
import string
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

# 랜덤 팀 타이틀 생성
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
driver.maximize_window()  # 브라우저 사이즈 최대화
driver.implicitly_wait(5)  # 암묵적 대기 Global

# Default Setting
# 멤버의 권한에 따라 Elements 의 속성이 다르기 때문에 멤버 권한에 따라 일부 스크립트를 수정해야 함
# 관리자 이상 = div[7],[8] / 정회원 = div[6],[7]

# 잔디 랜딩 접속 > 로그인
user_id = "dave.kim@tosslab.com"
user_pw = "@Worud1209"
by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').clear()  # 이메일 입력창 내용 비우기
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').send_keys(user_id)  # Email ID 입력
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys(user_pw)  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)

by_xpath('//*[@id="wrap"]/article/div/section[2]/button').click()  # + 팀 생성하기
by_selector('#body > div.modal.ng-isolate-scope.full-screen-modal.create-team-modal.in > div > div > '
            'div.full-screen-body.ng-scope > div > fieldset > div.jnd-input-box.input-name > input').send_keys(title)  # 팀 이름 입력
time.sleep(0.5)
by_selector('#body > div.modal.ng-isolate-scope.full-screen-modal.create-team-modal.in > div > div > '
            'div.full-screen-body.ng-scope > div > fieldset > div.jnd-input-box.input-team-name > input').send_keys(title)  # 팀 도메인 입력
time.sleep(1)
by_selector('#body > div.modal.ng-isolate-scope.full-screen-modal.create-team-modal.in > div > div > '
            'div.full-screen-actions.btn-container.ng-scope > button').click()  # 팀 생성 > 팀으로 이동하기
time.sleep(5)

team_title = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[1]/div[1]/div[2]/div[1]/span').text

print(team_title)
if title == team_title:
    print('팀 생성이 완료 되었습니다.')
else:
    print('팀 생성이 정상적으로 완료 되지 않았습니다. 팀 타이틀 또는 팀 생성 기능을 확인 하세요.')

esm = by_xpath('//*[@id="msgs_container"]/div[2]/div/div[2]/p').text
print(esm)
esm_chk = (title + "에 멤버를 초대하여" + "\n" + "대화를 시작해보세요")
print(esm_chk)
if esm == esm_chk:
    print('ESM 메시지가 정상적으로 출력되었습니다.')
else:
    print('ESM 메시지가 출력되지 않았습니다. 기본토픽을 확인 하세요.')

by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/ul/li/div[1]').click()  # 햄버거 메뉴 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/ul/li/div[2]/div[1]/ul/li[3]/span').click()  # 관리자 메뉴 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[3]/div[2]/aside/ul[1]/li[3]').click()  # 팀 관리 메뉴 클릭
by_xpath('//*[@id="mainContainerWrapper"]/team-manage/div/div[6]/a').click()  # 팀 삭제하기
del_noti = by_xpath('//*[@id="mainContainerWrapper"]/team-manage/div/div[6]/div[2]/div/span').text
del_noti_chk = ("정말로 팀을 삭제하시겠습니까?" + "\n" + "모든 메시지와 파일들이 삭제되며 복구할 수 없습니다.")
if del_noti == del_noti_chk:
    print('팀 삭제 경고 문구가 정상적으로 표시 되었습니다.')
else:
    print('FAIL!! 팀 삭제 경고 문구가 표시 되지 않았습니다.')

by_xpath('//*[@id="mainContainerWrapper"]/team-manage/div/div[6]/div[2]/form/div/input').send_keys(user_pw)  # pw 입력
by_xpath('//*[@id="mainContainerWrapper"]/team-manage/div/div[6]/div[2]/form/div/button').click()  # 팀 삭제하기
time.sleep(1)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button.btn.btn-red').click()  # 팀 삭제 확인
time.sleep(1)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button').click()  # 삭제 완료 확인
time.sleep(5)
try:
    main_chk = by_xpath('//*[@id="wrap"]/article/div/section[1]/header/h3/span').text
    if main_chk == '프로필':
        print('팀이 정상적으로 삭제 되어 잔디 메인으로 진입하였습니다.')
    else:
        print('FAIL!! 팀 삭제, 메인페이지 진입 또는 L10n을 확인하세요')
except:
    print('FAIL!! 팀이 정상적으로 삭제되지 않았습니다. 해당 기능을 확인하세요.')

print('팀 생성 & 삭제 테스트가 완료 되었습니다.')
print('테스트가 완료 되어 브라우저를 종료 합니다.')
driver.quit()
