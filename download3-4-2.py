from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
#소셜아이디 회원전환일수도 있고 로그인만 일수도 있다 분석을 잘해야됨 
#소셜 로그인 처리는 어떻게 해야되는가?
#로그인 유저정보 
LOGIN_INFO = {
    'user_id':'',
    'user_pw':''
}

#Sessoin 생성, with 구문안에서 유지 
with requests.Session() as s:
    login_req = s.post('',data=LOGIN_INFO)
    # #HTML 소스 확인 
    # print('login_req',login_req.text)
    # #Header 확인 
    # print('headers',login_req.headers)
    # 오류 났을수도 있으니 조건을 달아보자 
    if login_req.status_code == 200 and login_req.ok: #get 방식 
        post_one = s.get('')
        post_one.raise_for_status()#예외처리 
        soup = BeautifulSoup(post_one.text,'html.parser')
        # print(soup.prettify())#확인완료 
        