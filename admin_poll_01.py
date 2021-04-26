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
title = rm + rt + rn
# info_text = 'Selenium 에서 자동으로 생성된 토픽 입니다.'  # 토픽 설명으로 쓸 텍스트 변수 저장  < 에러겁나 나네...당분간 안씀

driver = webdriver.Chrome(executable_path="chromedriver.exe")  # 크롬드라이버 실행 경로 설정(상대경로) > 나중에 절대 경로로 바꿔야 함
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
driver.get("https://www.jandi.com")
driver.maximize_window()
driver.implicitly_wait(10)  # 암묵적 대기 Global

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
by_xpath('//*[@id="wrap"]/article/div/section[2]/article/ul/li[3]/div/button[2]/span/span').click()  # Dave Test.Team 으로 진입 (li[n] 숫자를 각 계정에 맞게 설정해야 함

# 자주 사용하는 요소의 XPath 값 저장해두기
m_input = by_xpath('//*[@id="message_input"]')  # 메시지 입력창을 "m_input" 변수에 저장

# 토픽 생성하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/i').click()  # 토픽 추가 메뉴 [+] 더보기 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[2]/div/aside/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/span').click()  # 새로운 토픽 생성하기 클릭
time.sleep(1)
by_xpath('//*[@id="topic-create-name"]').send_keys(title)  # 토픽 이름 입력
time.sleep(2)

# 토픽 설명 입력 스크립트는 에러율이 높아서 버림
# by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/form/div[1]/div[4]/div/div/textarea').click()
# by_xpath('//*[@id="jndApp"]/div[8]/div/div/div/form/div[1]/div[4]/div/div/textarea').send_keys(info_text)  # 토픽 설명 입력(정회원인 경우 div[7] 로 변경)
by_xpath('//*[@id="create_new_channel"]').click()  # 생성하기 클릭
time.sleep(2)
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

# 투표 생성
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[1]').click()  # [+] 업로드 버튼 클릭
by_xpath('//*[@id="cpanel"]/chat-panel/div/div/div/div[2]/div[3]/div[2]/div/section[5]/div/ul/li[2]').click()  # 투표 아이콘 클릭
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[2]/div/div[1]/div/div/input').send_keys('자동화 테스트 투표')  # 투표 제목 입력
by_xpath('//*[@id="poll_message_input"]').send_keys('자동화 테스트 툴을 투표해주세요 by.Selenium.')  # 투표 설명 입력
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[2]/div/div[3]/div/div/ul/li[1]/p/input').send_keys('Selenium' + Keys.ENTER)  # 보기1 입력하고 보기 하나더 추가
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[2]/div/div[3]/div/div/ul/li[2]/p/input').send_keys('Selenide' + Keys.ENTER)  # 보기2 입력하고 보기 하나더 추가
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[2]/div/div[3]/div/div/ul/li[3]/p/input').send_keys('Appium' + Keys.ENTER)  # 보기3 입력하고 보기 하나더 추가
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[2]/div/div[3]/div/div/ul/li[4]/p/input').send_keys('Automation Anywhere')  # 보기4 입력
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div[3]/button[2]').click()  # 투표 만들기 클릭
time.sleep(1)

# 투표 하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/ul/li[4]/a/i').click()  # 투표 아이콘 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[6]/div/div/div[2]/ul/li[1]/div').click()  # 투표 리스트 첫번째 투표 선택
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/fieldset/div/div[1]/ul/li[1]').click()  # 첫번째 보기 선택
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/fieldset/div/div[2]/button').click()  # 투표하기 버튼 클릭

# 재 투표 하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/a/i').click()  # 투표 상세 [...] 더보기 버튼 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/div/ul/li[1]/a/span').click()  # 재투표하기 클릭
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/fieldset/div/div[1]/ul/li[2]').click()  # 두번째 보기 선택
time.sleep(1)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/fieldset/div/div[2]/button').click()  # 재투표하기 버튼 클릭
time.sleep(1)

# 투표에 댓글 달기
r_input = by_xpath('//*[@id="detail_comment_input"]')  # 댓글 입력창을 "r_input" 변수에 저장
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/a/i').click()  # 투표 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/div/ul/li[2]/a/span').click()  # 댓글 메뉴 클릭하기
r_input.send_keys('Selenium에서 작성한 투표 댓글 입니다.' + Keys.ENTER)
time.sleep(0.5)
r_input.send_keys('@')
r_input.send_keys(Keys.ENTER)
r_input.send_keys('투표 멘션 댓글 테스트 메시지' + Keys.ENTER)
time.sleep(1)

# 투표 마감하기
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]').click()  # 투표 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/div/ul/li[3]').click()  # 투표 마감하기 메뉴 클릭
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div/button[1]').click()  # 투표 마감 취소 하기
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]').click()  # 투표 상세 [...] 더보기 버튼 클릭
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/ul/li[1]/div/ul/li[3]').click()  # 투표 마감하기 메뉴 클릭
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div/button[2]').click()  # 투표 마감 하기
time.sleep(5)
by_xpath('//*[@id="jndApp"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/i[2]').click()  # 투표 리스트 닫기
time.sleep(1)

# 토픽 삭제 하기
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[1]').click()  # 토픽 상단 더보기 메뉴 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[5]/div[2]/ul/li[3]/span').click()  # 토픽 삭제하기 메뉴 클릭
time.sleep(0.5)
by_xpath('//*[@id="jndApp"]/div[7]/div/div/div/div[2]/div/button[2]').click()  # 토픽 삭제 확인 다이얼로그 확인 클릭
time.sleep(0.5)
m_input.send_keys('토픽 테스트가 완료 되었습니다.' + Keys.ENTER)


m_input.send_keys('테스트가 완료 되어 브라우저를 종료 합니다.' + Keys.ENTER)
time.sleep(3)

driver.quit()