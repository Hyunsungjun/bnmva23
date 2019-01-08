#  /Users/hyeonseongjun/Desktop/mypro/chromedriver #geckodriver
#  /Users/hyeonseongjun/Desktop/mypro/phantomjs-2.1.1-macosx/bin/phantomjs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #cli환경 사용하는 옵션 
import time

class NcafeWriteAtt:
    #클래스 초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options() #한번만 사용할 것이기 때문에 self없이 한다 무분별하게 사용하면 리소스가 낭비된다 
        # chrome_options.add_argument("--headless")#CLI처리를 한다 User-agent에 헤드리스인것을 알려주기 때문에 보안성이 좋은 사이트는 ua를 넣어준다 
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="/Users/hyeonseongjun/Desktop/mypro/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인과 출석 체크 
    def writeAttendCheck(self):
        # pass #잠깐 쉬고 작업하기
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('awert_trewa')
        self.driver.find_element_by_name('pw').send_keys('gustjwns1@')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)#대기시간 그러나 페이지 완료되면 바로 넘어감 
        # self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=28949845&search.menuid=5')
        # self.driver.implicitly_wait(30)
        # #iframe때문에 제대로 값을 잡을수 없으므로 
        # self.driver.switch_to_frame('cafe_main')
        # self.driver.find_element_by_id('cmtinput').send_keys('ㅊㅊ')
        # self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
        # time.sleep(3)

    # 소멸자 
    def __del__(self):
        #self.driver.close() #현재 실행 포커스에 대해서 종료
        # self.driver.quit() #selenium 전체 프로그램 종료
        print("Removed driver Object")
# 실행 
if __name__ == '__main__':
    #객체 생성 
    a = NcafeWriteAtt()
    #시작 시간 
    start_time = time.time()
    #프로그램 실행 
    a.writeAttendCheck()
    #종료 시간 출력 
    print('---Total %s seconds ---'%(time.time() - start_time))
    #객체 소멸 
    # del a

    #캡챠때문에 진행이 안되므로 이건 여기서 스톱하고 다음에 머신러닝을 이용해서 로그인 해보도록 하겠다 