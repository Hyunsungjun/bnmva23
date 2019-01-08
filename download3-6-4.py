#  /Users/hyeonseongjun/Desktop/mypro/chromedriver #geckodriver
#  /Users/hyeonseongjun/Desktop/mypro/phantomjs-2.1.1-macosx/bin/phantomjs
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options #cli환경 사용하는 옵션 
import time
#CLI 환경 옵션
# chrome_options = Options()
# chrome_options.add_argument("--headless") # 내부적으론 이렇게 하면됨 
#모듈 임포트
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'/Users/hyeonseongjun/Desktop/mypro/chromedriver')
driver = webdriver.Chrome('/Users/hyeonseongjun/Desktop/mypro/chromedriver') #화면 볼꺼면 이모드로 하면됨 
#윈도우 창 사이즈 제어
# driver.set_window_size(1920,1280)
# driver.implicitly_wait(3)
ID = ''
PW = ''
#로그인 처리  구글
driver.get('https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.implicitly_wait(3)

#이자체를 예외처리로 넣어보자 안그래도 되겟다
#브라우저를 켜면 로그아웃 되기때문에 세션이 안남아 있으므로 계속 로그인 처리 가능 
#########################################################
#아이디 입력 
driver.find_element_by_id('identifierId').send_keys(ID)
driver.implicitly_wait(3)
ENTER = u'\ue007'
# time.sleep(3)
# driver.find_element_by_id('identifierId').send_keys(ENTER)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
driver.implicitly_wait(3)
#비밀번호 입력
driver.find_element_by_name('password').send_keys(PW)
driver.implicitly_wait(3)
# time.sleep(3)
driver.find_element_by_name('password').send_keys(ENTER)
#########################################################
#인프런 로그인
# driver.get("https://www.inflearn.com/wp-login.php?action=wordpress_social_authenticate&mode=login&provider=Google&redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")