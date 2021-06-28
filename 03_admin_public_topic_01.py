# 공개 토픽 테스트
# 정보수정, 멤버 초대, 멤버 내보내기, 토픽 관리자 변경, 토픽 나가기, 토픽 참여, 토픽 삭제
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
title1 = rand_str
print(title1)

driver = Chrome()  # 사용하는 디바이스의 OS 별로 지정한 PATH의 chromedriver 를 실행 할 수 있도록 환경변수 선언
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
by_selector = driver.find_element_by_css_selector  # 자주쓰는 스크립트를 간소화 하기
driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(5)  # 암묵적 대기 Global

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

print('공개 토픽 테스트를 시작합니다.')

# 토픽 생성하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/i').click()  # 토픽 추가 메뉴 [+] 더보기 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/span').click()  # 새로운 토픽 생성하기 클릭
time.sleep(1)
by_xpath('//*[@id="topic-create-name"]').send_keys(title1)  # 토픽 이름 입력
time.sleep(1)
public = by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/form/div[1]/div[3]/div/div/div[1]/dl[2]/label')
public.click()  # 공개 토픽으로 생성 선택
time.sleep(1)
by_xpath('//*[@id="create_new_channel"]').click()  # 생성하기 클릭
time.sleep(2)


# 토픽에 멤버 초대하기
title_chk1 = by_xpath('//*[@id="cpanel"]/nav/div/div[2]/div[1]/p').text  # 수정한 타이틀 추출
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
    by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button').click()  # 준회원 토픽 개수 초과 알럿 팝업 확인 클릭
    time.sleep(0.5)
except:
    time.sleep(0.5)
    by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button').click()  # 준회원 토픽 개수 초과 알럿 팝업 확인 클릭
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.topic-invite-modal.allowOverflowY.mc-theme-wh._modalContainer.in > '
            'div > div > div > div.modal-body > div.btn-box.txt-r > button.btn.btn-blue._modalSubmit.ng-binding').click()  # 초대하기 클릭
time.sleep(0.5)

#  토픽 정보 수정
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]').click()  # 토픽 상단 추가메뉴 호출
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[2]/span').click()  # 토픽 정보 변경하기 클릭
#  변경할 타이틀 재조합
n = 10
rand_str = ""
for i in range(n):
    rand_str += str(random.choice(string.ascii_uppercase + string.digits))
title2 = rand_str
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
# 자주 사용하는 요소의 XPath 값 저장해두기
m_input = by_xpath('//*[@id="message_input"]')  # 메시지 입력창을 "m_input" 변수에 저장
m_input.send_keys('토픽 설정 변경 테스트가 완료 되었습니다.' + Keys.ENTER)
time.sleep(1)

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
member_count = by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]/span').text
print(member_count)
if member_count == '1':
    m_input.send_keys('모든 멤버를 쫒아냈습니다!! *^^* ' + Keys.ENTER)
    print('모든 멤버를 쫒아냈습니다!! *^^*')
else:
    print('FAIL!! 멤버 내보내기에 실패 하였습니다. 해당 기능을 확인하세요.')
time.sleep(1)

# 토픽 나가기
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]/i').click()  # 토픽 상단 더보기 메뉴 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[4]').click()  # 토픽 나가기(토픽관리자)
time.sleep(1)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button.btn.btn-ok').click()  # 토픽관리자 권한 이양 확인
time.sleep(1)
admin_alone_chk = '이 토픽에 혼자 계셔서 토픽 관리자를 변경할 수 없습니다.'
admin_alone = by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[1]/div[3]/div/div/div/span').text
if admin_alone == admin_alone_chk:
    print('토픽에 혼자 있어서 토픽 관리자를 변경할 수 없습니다.', '멤버를 추가하고 다시 시도합니다.' + Keys.ENTER)
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[2]/button').click()  # 취소 버튼 클릭
    m_input.send_keys('토픽에 혼자 있어서 토픽 관리자를 변경할 수 없습니다.', '멤버를 추가하고 다시 시도합니다.')
    by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[4]').click()  # 멤버 초대하기 클릭
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]').click()  # 첫번째 멤버 선택
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div[2]/button[2]').click()  # 초대하기 클릭
    by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]/i').click()  # 토픽 상단 더보기 메뉴 클릭
    by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[4]').click()  # 토픽 나가기(토픽관리자)
    time.sleep(1)
    by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
                'div.btn-container > div > button.btn.btn-ok').click()  # 토픽관리자 권한 이양 확인
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[1]/div[3]/div/div/div/div').click()  # 토픽 관리자로 지정할 멤버 리스트 호출
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[1]/div[3]/div/div/div/div[2]/div[2]/div[2]/dl/dd/ul/div/li[1]').click()  # 첫번째 멤버 선택
    by_xpath('//*[@id="rename_channel"]').click()  # 완료 버튼 클릭
    time.sleep(5)
    m_input.send_keys('다른 멤버를 토픽 관리자로 지정하고 해당 공개 토픽에서 나왔습니다. JUMP 기능으로 다시 토픽에 진입하여 토픽을 삭제 합니다.' + Keys.ENTER)
else:
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[1]/div[3]/div/div/div/div').click()  # 토픽 관리자로 지정할 멤버 리스트 호출
    by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/form/div[1]/div[3]/div/div/div/div[2]/div[2]/div[2]/dl/dd/ul/div/li[1]').click()  # 첫번째 멤버 선택
    by_xpath('//*[@id="rename_channel"]').click()  # 완료 버튼 클릭
    time.sleep(5)
    m_input.send_keys('공개 토픽에서 나왔습니다. JUMP 기능으로 다시 토픽에 진입하여 토픽을 삭제 합니다.' + Keys.ENTER)

# 공개 토픽 재진입하기
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[2]/div/button').click()  # Jump 메뉴 클릭
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(title2)  # 검색할 토픽명 입력
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(Keys.ENTER)  # Enter 키 사용하여 검색한 토픽으로 진입
time.sleep(1)

# 토픽 삭제 하기
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]/i').click()  # 토픽 상단 더보기 메뉴 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[3]/span').click()  # 토픽 삭제하기 메뉴 클릭
time.sleep(0.5)
by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > '
            'div.btn-container > div > button.btn.btn-danger').click()  # 삭제 확인 다이얼로그 확인 버튼 클릭
time.sleep(5)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[1]/div[2]/div/button').click()  # Jump 메뉴 클릭
by_xpath('//*[@id="quick-launcher-filter"]').send_keys(title2)  # 검색할 토픽명 입력
tp_del = by_selector('#jndApp > div.modal.ng-isolate-scope.quick-launcher-modal._modalContainer.in > div > div > div > '
                     'div > div.quick-launcher-list > div.empty-matches > span').text  # 검색결과 없음 텍스트 Get
print(tp_del)
tp_del_chk = ("'" + title2 + "'" + "의 검색 결과가 없습니다.")
if tp_del == tp_del_chk:
    print('멤버가 있는 공개 보드 토픽을 정상적으로 삭제했습니다.')
else:
    print('FAIL!! 토픽이 삭제되지 않았습니다. 토픽 검색 또는 토픽 삭제 기능을 확인 하세요.')
Keys.ESCAPE
time.sleep(0.5)
print('공개 토픽 테스트가 정상적으로 완료 되었습니다.')
print('테스트가 완료 되어 브라우저를 종료 합니다.')

driver.quit()
