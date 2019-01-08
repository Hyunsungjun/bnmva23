#  /Users/hyeonseongjun/Desktop/mypro/chromedriver #geckodriver
#  /Users/hyeonseongjun/Desktop/mypro/phantomjs-2.1.1-macosx/bin/phantomjs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options #cli환경 사용하는 옵션 
import time
#CLI 환경 옵션
firefox_options = Options()
firefox_options.add_argument("--headless") # 내부적으론 이렇게 하면됨 
#모듈 임포트
driver = webdriver.Firefox(firefox_options=firefox_options,executable_path=r'/Users/hyeonseongjun/Desktop/mypro/geckodriver')
# driver = webdriver.Firefox('/Users/hyeonseongjun/Desktop/mypro/geckodriver') #화면 볼꺼면 이모드로 하면됨 
#윈도우 창 사이즈 제어
# driver.set_window_size(1920,1280)
driver.implicitly_wait(5)
#구글 스샷
driver.get('https://google.com')
# time.sleep(5)
driver.save_screenshot('/Users/hyeonseongjun/Desktop/inflearn/section2/test/websitef1.png')

driver.implicitly_wait(5)
#다음으로 이동해서 메인을 스샷
driver.get('https://www.daum.net')
# time.sleep(5)
driver.save_screenshot('/Users/hyeonseongjun/Desktop/inflearn/section2/test/websitef2.png')
driver.quit()
print("스크린샷 완료")
#결과적으로 펜텀으로도 충분히 다할수 있지만 cli환경을 이용해서 충분히 사용이 가능하다 