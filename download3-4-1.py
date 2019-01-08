from bs4 import BeautifulSoup
import requests

#로그인 유저정보 
LOGIN_INFO = {
    'user_id':'',
    'user_pw':''
}

#Sessoin 생성, with 구문안에서 유지 
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    # #HTML 소스 확인 
    # print('login_req',login_req.text)
    # #Header 확인 
    # print('headers',login_req.headers)
    # 오류 났을수도 있으니 조건을 달아보자 
    if login_req.status_code == 200 and login_req.ok: #get 방식 
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4609674&find=&ftext=')
        post_one.raise_for_status()#예외처리 
        soup = BeautifulSoup(post_one.text,'html.parser')
        # print(soup.prettify())#확인완료 
        article = soup.select_one("table:nth-of-type(3)").find_all('p')
        # print(article)#중간점검 
        for i in article:
            if i.string is not None:
                #DB INSERT, 엑셀로 저장, 텍스트 가공 이부분에서 해주며됨 
                print(i.text)