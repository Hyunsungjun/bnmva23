from bs4 import BeautifulSoup

#태그선택자를 알아보자

html = """
<html>
    <body>
        <ul>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
            <li><a href="http://www.google.com">google</a></li>
            <li><a href="http://www.tistory.com">tistory</a></li>
        </ul>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
#여기까진 똑가테~

links = soup.find_all("a")
#찾는다_전부(a태그를)
# print('links',type(links))#<class 'bs4.element.ResultSet'> resultset이네 참고

a = soup.find_all("a",string="daum")
print('a',a)
b = soup.find_all("a",limit=3)
#limit를 걸어 제한을 걸수있음 37번줄은 주석을 걸고 하고있다
print('b',b)
c = soup.find_all(string=["naver","google"])
print('c',type(c))


for a in links:
    # print('a',type(a),a)
    #이렇게 for문을 돌려 a태그를 전부 가져왔다
    href = a.attrs['href']
    #attrs 속성= attributes
    txt = a.string
    # print('txt >> ',txt,'href >> ',href)

#bs4를 이용해 키값이나 직접접근으로 사용할수있다