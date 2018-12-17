from bs4 import BeautifulSoup
import re #regex http://pythonstudy.xyz/python/article/401-정규-표현식-Regex


html = """
<html>
    <body>
        <ul>
            <li><a id="naver" href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
            <li><a href="https://www.google.com">google</a></li>
            <li><a href="https://www.tistory.com">tistory</a></li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
print(soup.find(id="naver").string)    #아이디 값을 가져올 수 있다
li = soup.find_all(href=re.compile(r"^https://"))
print('li',li)    #정규표현식을 써보니 https로 된 리스트값이 가져와졌다

for e in li:
    print(e.attrs['href'])
    #css selecter를 쓰면 되긴 하지만 정규표현식도 많이 쓰니 알아둘것