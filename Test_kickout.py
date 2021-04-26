import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")  # 크롬드라이버 실행 경로 설정(상대경로) > 나중에 절대 경로로 바꿔야 함
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
by_selector = driver.find_element_by_css_selector

driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(10)  # 암묵적 대기 Global

by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').clear()  # 이메일 입력창 내용 비우기
by_xpath('//*[@id="signin_form_container"]/form/div[1]/div[2]/input').send_keys('dave.kim@tosslab.com')  # Email ID 입력
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys('@Worud1209')  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)
by_xpath('//*[@id="wrap"]/article/div/section[2]/article/ul/li[3]/div/button[2]/span/span').click()  # Dave Test.Team 으로 진입 (li[n] 숫자를 각 계정에 맞게 설정해야 함

# 자주 사용하는 요소의 XPath 값 저장해두기
m_input = by_xpath('//*[@id="message_input"]')  # 메시지 입력창을 "m_input" 변수에 저장

# 그룹채팅 시작하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[3]/div[1]/div[2]/i').click()  # 채팅 리스트 [+]더보기 메뉴 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[3]/div[1]/div[2]/div/ul/li[1]/span').click()  # 채팅 시작하기
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 첫번째 멤버 선택하기 (이하 반복 9명까지)
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 2
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 3
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 4
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 5
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 6
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 7
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 8
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/h4').click()  # 9
time.sleep(1)
limit_chat = by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[1]/div/section[2]/div[2]/div/div/p/span').text  # 그룹챗 인원 제한 noti 텍스트 가져오기
limit_noti = "최대 10명까지만 그룹 채팅방에 참여하실 수 있습니다."
if limit_chat == limit_noti:
    print('그룹챗 인원 제한 노티가 정상적으로 발생하였습니다.')
else:
    print('그룹챗 인원 제한 노티를 확인하세요.')
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/div[2]/div[2]/button[2]').click()  # 대화 시작하기
time.sleep(1)
#  멤버 내보내기 1 &
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(1)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인

time.sleep(0.5)
#  멤버 내보내기 2
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 3
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 4
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 5
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 6
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 7
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 8
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
#  멤버 내보내기 9
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[2]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 내보내기 확인
time.sleep(0.5)
m_input.send_keys('모든 멤버를 쫒아냈습니다!! *^^* ' + Keys.ENTER)
time.sleep(0.5)
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[4]/div[1]/i').click()  # 토픽 메뉴 호출
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[4]/div[2]/ul/li[3]').click()  # 채팅방 나가기
time.sleep(0.5)
kickout_accept = by_selector('#jndApp > div.modal.fade.ng-isolate-scope.center-dialog-modal.mc-theme-wh.in > div > div > div > div.btn-container > div > button.btn.btn-ok').click()  # 채팅방 나가기 확인
time.sleep(3)
m_input.send_keys('그룹채팅 테스트가 완료 되어 브라우저를 종료 합니다.' + Keys.ENTER)

driver.quit()
