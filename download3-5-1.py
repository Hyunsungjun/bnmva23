from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
# https://pypi.python.org/pypi/fake-UserAgent
#위시켓 로그인처리 고급과정 

URL = 'https://www.wishket.com/accounts/login/'
#csrftoken값이 맞아야 해서 보안성이 높은 편이다 

#Fake User-Agent 생성 
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s:
    #URL 연결 
    s.get(URL)
    #Login 정보 PayLoad
    LOGIN_INFO = {
        'identification':'ubih1un',
        'password':'doo11trm',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # #token값이 나오는지 확인 #랜덤이므로 값이 계속 바뀜 
    # print('token',s.cookies['csrftoken'])
    #헤더 정보 확인 
    # print('headers',s.headers)

    #요청 
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome),'Referer':'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인 
    # print('response',response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        print(projectList)
        for i in projectList:
            print(i.find('th').string,i.find('td').text)
# 정리 
# 로그인하는데 암호화가 되어있으면 헤더나 유저정보,토큰 등을 확인해서 만들어야 한다 
# 즉 403에러가 났을때 왜 에러가 났는지 파악을 해보는것이 중요하다 