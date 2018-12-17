from bs4 import BeautifulSoup
import urllib.request as req

url = "http://finance.daum.net/"
# url = "Daum 금융.html"
res = req.urlopen(url).read() #이걸 왜썼는지 다시 공부해서 정리해놓자
soup = BeautifulSoup(res,"html.parser")

# print('soup',soup.prettify()) #잘되는가 확인

top = soup.select("div#boxTopSectors > div > ul > li > a")
# for li in top:
#     print('li>>',li.text)
print('아이고 출력중입니다',top)
##################################### 비동기 방식으로 더이상 동작하지 않음