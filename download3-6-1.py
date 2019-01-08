#  /Users/hyeonseongjun/Desktop/mypro/chromedriver #geckodriver
#  /Users/hyeonseongjun/Desktop/mypro/ghostdriver-master/bin/ghostdriver
from selenium import webdriver
#모듈 임포트
driver = webdriver.PhantomJS('/Users/hyeonseongjun/Desktop/mypro/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.implicitly_wait(5)
#구글 스샷
driver.get('https://google.com')
driver.save_screenshot('/Users/hyeonseongjun/Desktop/inflearn/section2/test/website1.png')

driver.implicitly_wait(5)
#다음으로 이동해서 메인을 스샷
driver.get('https://www.daum.net')
driver.save_screenshot('/Users/hyeonseongjun/Desktop/inflearn/section2/test/website2.png')
driver.quit()
print("스크린샷 완료")
