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

# 토픽 생성하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/i').click()  # 토픽 추가 메뉴 [+] 더보기 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/span').click()  # 새로운 토픽 생성하기 클릭
time.sleep(1)
by_xpath('//*[@id="topic-create-name"]').send_keys(title)  # 토픽 이름 입력
time.sleep(1)
by_xpath('//*[@id="create_new_channel"]').click()  # 생성하기 클릭
time.sleep(2)

# 방금 생성한 토픽으로 점프 하기 (토픽이 제대로 생성되었는지와 점프 기능 동시에 확인 가능)
by_xpath('//*[@id="topic-21183818"]/div/div/div/h5').click()  # 기본 토픽으로 이동
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[2]/div/button').click()  # Jump 메뉴 클릭
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(title)  # 검색할 토픽명 입력
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(Keys.ENTER)  # Enter 키 사용하여 검색한 토픽으로 진입
time.sleep(1)
by_xpath('//*[@id="msgs_container"]/div[2]/div/div[3]/button').click()  # 멤버 초대하기 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[1]/ul/li[1]/div/input').send_keys('김대웅')  # 검색 할 멤버 입력
time.sleep(1)

# 아래는 Dave Test.Team 에서만 사용 가능한 준회원 토픽수 5개 제한 확인 스크립트
try:
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 첫번째 '김대웅' 선택
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 두번째 '김대웅 자동화 Dave' 선택
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 세번째 '김대웅 테스트' 선택
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 네번째 '김대웅_5개 토픽' 선택(준회원 5개 토픽 초과 멤버)
    time.sleep(0.5)
    by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button').click()  # 준회원 토픽 개수 초과 알럿 팝업 확인 클릭
    time.sleep(0.5)
except:
    time.sleep(0.5)
    by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button').click()  # 준회원 토픽 개수 초과 알럿 팝업 확인 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.topic-invite-modal.allowOverflowY.mc-theme-wh._modalContainer.in > '
            'div > div > div > div.modal-body > div.btn-box.txt-r > button.btn.btn-blue._modalSubmit.ng-binding').click()  # 초대하기 클릭
time.sleep(0.5)

# 메시지 전송 테스트
m_input.send_keys('Selenium 에서 보내는 테스트 메시지 입니다.' + Keys.ENTER)  # 테스트 메시지 전송
time.sleep(1)

# 스티커 전송 테스트
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[2]/div[2]/div[1]/div/button/i').click()  # 스티커 모달 아이콘 클릭
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[1]/div/i').click()  # 최근 사용한 스티커 카테고리 클릭
time.sleep(1)
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[2]/div[4]/div[1]/ul/li[1]/div').click()  # 첫번째 스티커 클릭
m_input.send_keys(Keys.ENTER)  # 메시지 전송 버튼 클릭

# 멘션 테스트
# 멘션리스트는 element 값을 찾을 수 없기 때문에 키보드 컨트롤을 이용하여 자동화 함
m_input.send_keys('@all')  # all 멘션
m_input.send_keys(Keys.ENTER)
m_input.send_keys('Selenium 에서 보내는 테스트 멘션 메시지 입니다.' + Keys.ENTER)  # 테스트 메시지 전송

# 할 일 생성 테스트
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[1]').click()  # [+] 업로드 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[2]/div/section[5]/div/ul/li[1]/i').click()  # 할 일 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/section[1]/button').click()  # 할 일 생성 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]/div/dl[2]/dd/div/textarea').send_keys('Selenium 에서 생성한 테스트 할 일 입니다.')  # 할 일 타이틀 입력
by_xpath('//*[@id="tool-todo-description-editor"]').send_keys('Selenium 에서 생성할 테스트 할 일 입니다.')  # 할 일 설명 입력
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[5]/button[2]').click()  # 할 일 저장 클릭
time.sleep(5)  # 할 일 생성완료 팝업 사라질때 까지 대기 > 이거 컨트롤 하는 방법이 있을까?
m_input.send_keys('할 일이 생성 되었습니다.' + Keys.ENTER)  # 할 일 생성 메시지 전송

# 할 일 수정_진척률
by_xpath('//*[@id="tool-todo-list"]/div[1]/div[1]').click()  # 현재 보이는 할 일 리스트에서 첫번째 할 일 선택
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em').click()  # 할 일 진척률 클릭
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em/div/ul/li[2]/span').click()  # 진행 25% 클릭
time.sleep(2)
rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '25%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 정상적으로 반영되었습니다.' + Keys.ENTER)
    print('할 일 진척율 25%')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 진척율을 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em').click()  # 할 일 진척률 클릭
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em/div/ul/li[3]/span').click()  # 진행 50% 클릭
time.sleep(2)

rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '50%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 정상적으로 반영되었습니다.' + Keys.ENTER)
    print('할 일 진척율 50%')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 진척율을 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em').click()  # 할 일 진척률 클릭
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em/div/ul/li[4]/span').click()  # 진행 75% 클릭
time.sleep(2)

rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '75%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 정상적으로 반영되었습니다.' + Keys.ENTER)
    print('할 일 진척율 75%')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 진척율을 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em').click()  # 할 일 진척률 클릭
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em/div/ul/li[1]/span').click()  # 대기 0% 클릭
time.sleep(2)

rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '0%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 정상적으로 반영되었습니다.' + Keys.ENTER)
    print('할 일 진척율 0%')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 진척율을 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em').click()  # 할 일 진척률 클릭
by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[1]/dl[2]/dd/div/div/em/div/ul/li[5]/span').click()  # 완료 100% 클릭
time.sleep(2)

rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '100%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('할 일이 정상적으로 완료 처리 되었습니다.' + Keys.ENTER)
    print('할 일이 정상적으로 완료 처리 되었습니다.')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 진척율을 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/i[1]').click()  # 뒤로가기
time.sleep(1)

# 할 일 재개후 수정 테스트
by_xpath('//*[@id="tool-todo-list"]/div[1]/div[1]').click()  # 현재 보이는 할 일 리스트에서 첫번째 할 일 선택
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/i').click()  # 할 일 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[4]/a/span').click()  # 할 일 재개 메뉴 클릭
time.sleep(2)

rate = by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/em/em').text  # 할 일 상세의 진척율을 gettext 로 'rate' 저장
print(rate)
r = '0%'
if rate == r:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 정상적으로 반영되었습니다.' + Keys.ENTER)
    print('할 일이 재개되었습니다.')
else:
    by_xpath('//*[@id="detail_comment_input"]').send_keys('진척율이 실제 진척율과 다릅니다.' + Keys.ENTER)
    print('FAIL!! 할 일 재개에 실패하였습니다. 진척율 또는 할 일 메뉴를 확인 하세요!!')
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/i').click()  # 할 일 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[3]/a/span').click()  # 할 일 수정 메뉴 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]/div/dl[2]/dd/div/textarea').clear()  # 할 일 타이틀 지우기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]/div/dl[2]/dd/div/textarea').send_keys('Selenium 자동화로 수정된 타이틀 입니다.')  # 할 일 타이틀 수정
by_xpath('//*[@id="tool-todo-description-editor"]').clear()  # 할 일 설명 지우기
by_xpath('//*[@id="tool-todo-description-editor"]').send_keys('Selenium 에서 설명을 수정 하였습니다.Selenium 에서 설명을 수정 하였습니다.Selenium 에서 설명을 수정 하였습니다.')  # 할 일 설명 수정
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[1]/dd/div[3]/button').click()  # 담당자 관리 버튼 클릭
try:
    by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[1]/dd/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/label/div/p').click()  # 2열 담당자 선택

    by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[1]/dd/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[3]/label/div/p').click()  # 3열 담당자 선택
    by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[1]/dd/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[4]/label/div/p').click()  # 4열 담당자 선택
except:
    by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
                'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
                'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > div > div.todo-detail.is-expande > '
                'dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > div > div.custom-member-buttons > button:nth-child(2)').click()  # 담당자 설정 버튼 클릭

by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
            'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
            'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > div > div.todo-detail.is-expande > '
            'dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > div > div.custom-member-buttons > button:nth-child(2)').click()  # 담당자 설정 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[3]/dd/div/div').click()  # 알림 설정 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[3]/dd/div/div[2]/div/div').click()  # 알림 드랍 박스 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[1]/dl[3]/dd/div/div[2]/div/ul/li[2]').click()  # 정시 클릭
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[5]/button[2]').click()  # 저장하기 버튼 클릭
time.sleep(5)  # 할 일 생성완료 팝업 사라질때 까지 대기 > 이거 컨트롤 하는 방법이 있을까?
by_xpath('//*[@id="tool-todo-list"]/div[1]/div[1]').click()  # 현재 보이는 할 일 리스트에서 첫번째 할 일 선택
alarm = by_xpath('//*[@id="tool-todo-detail-content-base"]/div/div[2]/dl[2]/dd/p/span').text
alram_chk = '정시'
if alarm == alram_chk:
    print('알람 설정이 정상적으로 저장되었습니다.')
else:
    print('FAIL!! 알람 설정이 저장되지 않았습니다.')
    m_input.send_keys('FAIL!! 알람 수정이 되지 않았습니다. 할 일 수정 기능을 확인 하세요.' + Keys.ENTER)  # 할 일 생성 메시지 전송
m_input.send_keys('할 일이 수정 되었습니다.' + Keys.ENTER)  # 할 일 생성 메시지 전송
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/i[1]').click()  # 뒤로가기 버튼 클릭(할 일 리스트로 돌아가기)
time.sleep(0.5)

# 할 일 재개 후 담당자 일부 삭제
by_xpath('//*[@id="tool-todo-list"]/div[1]/div[1]').click()  # 현재 보이는 할 일 리스트에서 첫번째 할 일 선택
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/i').click()  # 할 일 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[3]/a/span').click()  # 할 일 수정 메뉴 클릭
by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
            'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > '
            'div.tool-list.tool-view > div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > '
            'div > div.todo-detail.is-expande > dl:nth-child(1) > dd > div.flex-row-box.flex-end.ng-scope > button').click()  # 담당자 관리 버튼 클릭(수정 할 때는 div[6]버튼)
time.sleep(0.5)
try:
    by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
                'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
                'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > div > '
                'div.todo-detail.is-expande > dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > '
                'div > div.custom-opt-view.opt-def._container.ng-scope > div.ng-isolate-scope > dl > dd > ul > div > li:nth-child(3)').click()  # 3열 담당자 선택
    by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
                'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
                'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > div > '
                'div.todo-detail.is-expande > dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > '
                'div > div.custom-opt-view.opt-def._container.ng-scope > div.ng-isolate-scope > dl > dd > ul > div > li:nth-child(4)').click()  # 4열 담당자 선택
except:
    by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
                'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
                'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > '
                'div > div.todo-detail.is-expande > dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > '
                'div > div.custom-member-buttons > button:nth-child(2)').click()  # 담당자 설정 버튼 클릭
by_selector('#jndApp > div.content-wrapper.opac-in-fast._contentWrapper.ng-isolate-scope > div.body-wrapper.has-banner > '
            'div.rpanel.shadow.non-selectable._toolPanel > div.file.ng-scope.scroll_gray.opac_in.extend > div > div.tool-list.tool-view > '
            'div.file-detail-content.todo-detail-content.ng-scope > div.todo-detail-body._detailBody._scrollContainer > '
            'div > div.todo-detail.is-expande > dl:nth-child(1) > dd > div.custom-select-box-wrap.jnd-member-select._selectbox.blur-effect.ng-isolate-scope > '
            'div > div.custom-member-buttons > button:nth-child(2)').click()  # 담당자 설정 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[5]/button[2]').click()  # 저장하기 버튼 클릭
time.sleep(5)  # 할 일 생성완료 팝업 사라질때 까지 대기 > 이거 컨트롤 하는 방법이 있을까?
m_input.send_keys('할 일 담당자가 일부 삭제 되었습니다.' + Keys.ENTER)  # 할 일 생성 메시지 전송
time.sleep(1)

# 할 일 생성 및 삭제 테스트
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[1]').click()  # [+] 업로드 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[2]/div/section[5]/div/ul/li[1]/i').click()  # 할 일 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/section[1]/button').click()  # 할 일 생성 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]/div/dl[2]/dd/div/textarea').send_keys('Selenium 에서 생성한 테스트 할 일 입니다.')  # 할 일 타이틀 입력
by_xpath('//*[@id="tool-todo-description-editor"]').send_keys('Selenium 에서 생성할 테스트 할 일 입니다.')  # 할 일 설명 입력
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[5]/button[2]').click()  # 할 일 저장 클릭
time.sleep(5)  # 할 일 생성완료 팝업 사라질때 까지 대기 > 이거 컨트롤 하는 방법이 있을까?
m_input.send_keys('할 일이 생성 되었습니다.' + Keys.ENTER)  # 할 일 생성 메시지 전송
by_xpath('//*[@id="tool-todo-list"]/div[1]/div[1]').click()  # 현재 보이는 할 일 리스트에서 첫번째 할 일 선택
time.sleep(2)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/i').click()  # 할 일 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[4]/a/span').click()  # 할 일 삭제 메뉴 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button.btn.btn-danger').click()  # 삭제 확인 다이얼로그 확인 버튼 클릭
time.sleep(5)
todo_del = by_xpath('//*[@id="tool-todo-list"]/div[1]/div[2]/strong').text  # 할 일 리스트에서 첫번째 할 일의 타이틀 가져옴
todo_del_chk = ('Selenium 에서 생성한 테스트 할 일 입니다.')  # 삭제했던 토픽과 리스트 첫번째 할 일의 타이틀 비교
if todo_del == todo_del_chk:
    print('FAIL!! 할 일이 삭제 되지 않았습니다. 할 일 리스트 또는 할 일 삭제메뉴를 확인하세요')  # 같으면 삭제 되지 않은것으로 판단
else:
    print('할 일이 정상적으로 삭제 되었습니다.')  # 다르면 삭제된 것으로 판단
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/i[1]').click()  # 할 일 리스트 닫기
m_input.send_keys('할 일이 삭제 되었습니다.' + Keys.ENTER)  # 할 일 삭제 메시지 전송

# 토픽 삭제 하기
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]/i').click()  # 토픽 상단 더보기 메뉴 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[3]/span').click()  # 토픽 삭제하기 메뉴 클릭
time.sleep(0.5)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button.btn.btn-danger').click()  # 삭제 확인 다이얼로그 확인 버튼 클릭
time.sleep(5)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[2]/div/button').click()  # Jump 메뉴 클릭
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(title)  # 검색할 토픽명 입력
tp_del = by_selector('#jndApp > div.modal.ng-isolate-scope.quick-launcher-modal._modalContainer.in > div > div > div > '
                     'div > div.quick-launcher-list > div.empty-matches > span').text  # 검색결과 없음 텍스트 Get
print(tp_del)
tp_del_chk = ("'" + title + "'" + "의 검색 결과가 없습니다.")
if tp_del == tp_del_chk:
    print('토픽이 정상적으로 삭제 되었습니다.')
else:
    print('FAIL!! 토픽이 삭제되지 않았습니다. 토픽 검색 또는 토픽 삭제 기능을 확인 하세요.')
Keys.ESCAPE
print('할 일 테스트가 완료 되었습니다.')
print('테스트가 완료 되어 브라우저를 종료 합니다.')
time.sleep(3)

driver.quit()
