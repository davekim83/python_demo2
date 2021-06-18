# 로그인 테스트
# Author : Dave

import time
from selenium.webdriver import Chrome

driver = Chrome()  # 사용하는 디바이스의 OS 별로 지정한 PATH의 chromedriver 를 실행 할 수 있도록 환경변수 선언

by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
driver.get("https://www.jandi.com")
driver.maximize_window()
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
login_chk = by_xpath('//*[@id="wrap"]/article/div/section[1]/article/dl/dt/span').text
id = "Dave.KIM"
if id == login_chk:
    print('정상적으로 로그인 되었습니다.')
else:
    print('로그인이 되지 않았거나 프로필 정보를 불러오지 못했습니다.')
time.sleep(1)
by_xpath('//*[@id="wrap"]/header/nav/ul/li[2]').click()  # 프로필 드랍다운 메뉴
by_xpath('//*[@id="wrap"]/header/nav/ul/li[2]/div/ul/li[2]').click()  # 로그아웃
time.sleep(2)
logout_chk1 = by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').text
logout_flag = "로그인"
if logout_chk1 == logout_flag:
    print('정상적으로 로그아웃 되었습니다.')
else:
    print('Fail!! 로그아웃 되지 않았거나 페이지 정보를 불러오지 못했습니다.')
time.sleep(1)

# 이메일 입력 없이 로그인('이메일 기억하기' 상태라면 ID input 영역에 이메일이 남아 있어야 함)
by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys(user_pw)  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(2)
login_chk = by_xpath('//*[@id="wrap"]/article/div/section[1]/article/dl/dt/span').text
id = "Dave.KIM"
if id == login_chk:
    print('로그인 성공. 이메일 기억하기 정상 동작')
else:
    print('이메일 기억하기 오류 또는 로그인이 정상적이지 않습니다.')
time.sleep(1)
by_xpath('//*[@id="wrap"]/header/nav/ul/li[2]').click()  # 프로필 드랍다운 메뉴
by_xpath('//*[@id="wrap"]/header/nav/ul/li[2]/div/ul/li[2]').click()  # 로그아웃
time.sleep(2)
logout_chk2 = by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').text
if logout_chk2 == logout_flag:
    print('정상적으로 로그아웃 되었습니다.')
else:
    print('Fail!! 로그아웃 되지 않았거나 페이지 정보를 불러오지 못했습니다.')
time.sleep(1)

by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[4]/input').click()  # 이메일 기억하기 해제
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys(user_pw)  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)
by_xpath('//*[@id="wrap"]/article/div/section[2]/article/ul/li[3]/div/button[2]/span/span').click()  # Dave Test.Team 으로 진입 (li[n] 숫자를 각 계정에 맞게 설정해야 함
time.sleep(3)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/ul/li/div[1]/i').click()  # 햄버거 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/ul/li/div[2]/div[4]/ul/li[2]').click()  # 로그아웃 클릭
time.sleep(2)
by_xpath('//*[@id="jnd-header"]/nav/div[2]/div[2]/ul[2]/li/button').click()  # 로그인 버튼 클릭
by_xpath('//*[@id="signin_form_container"]/form/div[2]/div[2]/input').send_keys(user_pw)  # PW 입력
by_xpath('//*[@id="signin_form_container"]/form/button').click()  # 로그인 버튼 클릭
time.sleep(3)
try:
    login_chk = by_xpath('//*[@id="wrap"]/article/div/section[1]/article/dl/dt/span').text
    id = "Dave.KIM"
    if id == login_chk:
        print('이메일 기억하기 설정 해제되지 않음')
except:
    print('이메일 기억하기 설정해제 정상 동작')
time.sleep(3)
print('로그인 테스트가 정상적으로 완료 되었습니다.')
print('테스트가 완료 되어 브라우저를 종료 합니다.')

driver.quit()
