from bs4 import BeautifulSoup

#CSS선택자를 가장 많이 사용한다
#https://www.w3schools.com/cssref/trysel.asp

html = """
<html>
    <body>
        <div id="main">
            <h1>강의목록</h1>
            <ul class="lecs">
                <li>Java 초고수 되기</li>
                <li>파이썬 기초 프로그래밍</li>
                <li>파이썬 머신러닝 프로그래밍</li>
                <li>안드로이드 블루투스 프로그래밍</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
# h1 = soup.select("div#main > h1")
# #dvi에 아이디가 main인것 하위에 h1
# print('h1',h1)
# print(h1.string) #에러가 납니다 
# #이유는 리스트 형태로 가져오기 때문에 문자열로 전환할수가 없는거다 그래서
# for z in h1:
#     print(z.string)
#     #이런 형태로 가져와야되는데 번거롭다

#그래서 select_one으로 하나만 가져오면 직접 출력이 가능해지는데
h1 = soup.select_one("div#main > h1")
print('h1',h1.string)
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>",li.string)
    #크롬 도구에서도 추출해줌
    