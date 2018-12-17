from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read() #이걸 왜썼는지 다시 공부해서 정리해놓자
soup = BeautifulSoup(res,"html.parser")

top4 = soup.select("#siselist_tab_0 > tr")
# print(top4)#하나만 가져오네
# for e in top4:
#     # print(e)#for문 왜쓰나 했더니 전부다 가져옴옴
#     print(e.find("a"))#a태그 찾기

# for i,e in enumerate(top4):#이렇게 i를 줄수 있지만 None에 1이 걸려버리므로 변수를 선언하기로 한다
#     if e.find("a") is not None:
#         print(i,e.select_one(".tltle").string)

i=1
for e in top4:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 2#파이썬에서 i++; 인듯
        