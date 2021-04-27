# 비공개 토픽 멤버 초대 및 정보 수정 테스트
# 5.14 inner API 변경 대응 테스트
# Author : Dave

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 랜덤 토픽 타이틀 생성
rm = random.sample(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 1)
rt = random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 5)
rn = random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 2)
random.shuffle(rt)
random.shuffle(rn)
title1 = rm + rt + rn
print(title1)
# info = 'Selenium 에서 자동으로 생성된 토픽 입니다.'  # 토픽 설명으로 쓸 텍스트 변수 저장  < 에러겁나 나네...당분간 안씀

driver = webdriver.Chrome(executable_path="chromedriver.exe")  # 크롬드라이버 실행 경로 설정(상대경로) > 나중에 절대 경로로 바꿔야 함
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
by_selector = driver.find_element_by_css_selector  # 자주쓰는 스크립트를 간소화 하기
driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(10)  # 암묵적 대기 Global

# Default Setting
# 멤버의 권한에 따라 Elements 의 속성이 다르기 때문에 멤버 권한에 따라 일부 스크립트를 수정해야 함
# 관리자 이상 = div[7],[8] / 정회원 = div[6],[7]

# 잔디 랜딩 접속 > 로그인
user_id = 'dave.kim@tosslab.com'
user_pw = '@Worud1209'
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
by_xpath('//*[@id="topic-create-name"]').send_keys(title1)  # 토픽 이름 입력
time.sleep(1)
by_xpath('//*[@id="create_new_channel"]').click()  # 생성하기 클릭
time.sleep(2)

# 토픽에 멤버 초대하기
title_chk1 = by_xpath('//*[@id="cpanel"]/nav/div/div[2]/div[1]/p').text  # 수정한 타이틀 추출
by_xpath('//*[@id="msgs_container"]/div[2]/div/div[3]/button').click()  # 멤버 초대하기 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[1]/ul/li[1]/div/input').send_keys('김대웅')  # 검색 할 멤버 입력
time.sleep(1)

# 아래는 Dave Test.Team 에서만 사용 가능한 스크립트
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 첫번째 '김대웅' 선택
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 두번째 '김대웅 자동화 Dave' 선택
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 세번째 '김대웅 테스트' 선택
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 네번째 '김대웅_5개 토픽' 선택(준회원 5개 토픽 초과 멤버)
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div/button').click()  # 준회원은 최대 5개의 토픽에만 참여가 가능합니다. 알럿 팝업 확인 클릭
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[2]/button[2]').click()  # 초대하기 클릭
time.sleep(0.5)

#  토픽 정보 수정
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]').click()  # 토픽 상단 추가메뉴 호출
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[2]/span').click()  # 토픽 정보 변경하기 클릭
#  변경할 타이틀 재조합
random.shuffle(rt)
random.shuffle(rn)
title2 = rm + rt + rn
print(title2)
by_xpath('//*[@id="topic-rename-name"]').clear()  # 타이틀 입력란 지움
by_xpath('//*[@id="topic-rename-name"]').send_keys(title2)  # 새로 조합한 타이틀 입력
topic_info = '토픽 설명 수정 테스트 입니다.'
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.mc-theme-wh._modalContainer.in > div > div > div > form > '
            'div.modal-body.topic-rename > div.form-horizontal.topic-description-container > div > div > textarea').send_keys('토픽 설명 수정 테스트 입니다.')  # 토픽 설명 추가
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.mc-theme-wh._modalContainer.in > div > div > div > form > '
            'div.modal-body.topic-rename > div.form-horizontal.topic-option-container > div > div > span > span').click()  # 더보기 클릭
time.sleep(1)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.mc-theme-wh._modalContainer.in > div > div > div > form > div.modal-body.topic-rename > '
            'div.form-horizontal.topic-option-container > div > div > div > div.form-horizontal.option-read-only.ng-scope > div > label > div').click()  # 읽기 전용 설정 클릭
time.sleep(1)
by_xpath('//*[@id="rename_channel"]').click()  # 완료 클릭
time.sleep(1)
title_chk2 = by_xpath('//*[@id="cpanel"]/nav/div/div[2]/div[1]/p').text  # 수정한 타이틀 추출
if title_chk1 == title_chk2:  # 입력한 타이틀과 추출한 타이틀 비교
    print('FAIL!! 공개 토픽 타이틀이 변경되지 않았습니다.')
else:
    print('공개 토픽 타이틀이 정상적으로 변경 되었습니다.')
time.sleep(1)
topic_info_chk = by_xpath('//*[@id="cpanel"]/nav/div/div[2]/div[2]/span/span').text  # 수정한 설명 추출
if topic_info == topic_info_chk:  # 입력한 설명과 추출한 설명 비교
    print('공개 토픽 설명이 정상적으로 변경 되었습니다.')
else:
    print('FAIL!! 공개 토픽 설명이 변경되지 않았습니다.')
time.sleep(1)
try:
    read_only = by_xpath('//*[@id="cpanel"]/nav/div/div[2]/div[2]/span[1]').text
    print(read_only + ' 설정이 변경 되었습니다.')
except:
    print('읽기 전용 설정이 되지 않았습니다.')
time.sleep(1)
m_input.send_keys('테스트가 완료 되었습니다.' + Keys.ENTER)
time.sleep(1)

driver.quit()

