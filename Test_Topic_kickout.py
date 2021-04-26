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

driver = webdriver.Chrome(executable_path="chromedriver.exe")  # 크롬드라이버 실행 경로 설정(상대경로) > 나중에 절대 경로로 바꿔야 함
by_xpath = driver.find_element_by_xpath  # 자주쓰는 스크립트를 간소화 하기
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
by_xpath('//*[@id="jndApp"]/div[6]/div/div/div/div[2]/div/button[2]').click()  # 다이얼로그 확인 클릭
time.sleep(1)
# 토픽 멤버 내보내기 2
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/a').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
by_xpath('//*[@id="jndApp"]/div[6]/div/div/div/div[2]/div/button[2]').click()  # 다이얼로그 확인 클릭
time.sleep(1)
# 토픽 멤버 내보내기 3
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[1]').click()  # 참여 멤버 버튼 클릭
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/a').click()  # 2열 멤버 선택
by_xpath('//*[@id="cpanel"]/nav/div/div[3]/ul/li[3]/div[2]/div/div[2]/div[2]/dl/dd/ul/div/li[2]/div/div[2]/span').click()  # 내보내기 클릭
by_xpath('//*[@id="jndApp"]/div[6]/div/div/div/div[2]/div/button[2]').click()  # 다이얼로그 확인 클릭
time.sleep(1)
m_input.send_keys('모든 멤버를 쫒아냈습니다!! *^^* ' + Keys.ENTER)
m_input.send_keys('테스트가 완료 되어 브라우저를 종료 합니다.' + Keys.ENTER)
time.sleep(3)

driver.quit()
