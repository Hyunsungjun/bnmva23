#HTML은 지정된 태그만 사용이 가능 
#XML은 SGML어와 HTML의 장점을 혼합한게 XML이다 
#XML의 설계원칙은 인터넷에서 쉽게 처리속도도 빨라야 한다 
#그리고 문서작성이 용이하고 가독성이 좋고 어렵지 않아야 한다 
#XML프로그램을 쉽게 작성하여야 한다 

import urllib.request as req #다운 
from bs4 import BeautifulSoup
import os.path

# 다운로드 URL 
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/forecast.xml"

# 파일 확인 if 만약 not 없으면 os savename경로에 다운을 받는다 
if not os.path.exists(savename):
    req.urlretrieve(url, savename) #두번째부턴 받지않음 
    print('다운로드 완료')

# BeautiFulSoup 파싱 
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')#html성격을 다갖고있으므로 

# 지역확인 <도시별 최저온도>
info = {}
for location in soup.find_all("location"):#xml은 find가 나음
    loc = location.find("city").string
    # print(loc) #도시만 가져오는걸 확인
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
# print(info)
# print(info.keys())#알아서 리스트 처리해줌 암시적 
# print(sorted(info.keys()))
# print(info.values())

# 각 지역별 날씨 텍스트 쓰기 
with open('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/forecast.txt','wt') as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:#바로 딕셔너리 형태의
            print("-",n)
            f.write('\t'+str(n)+'\n')

# XML : https://www.w3schools.com/xml/default.asp
# Bs4 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
