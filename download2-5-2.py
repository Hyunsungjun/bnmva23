from bs4 import BeautifulSoup
#html 예시로 만듬
html = """
<html>
<body>
<h1>파이썬 beautifulsoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html> 
"""
# print('html',html) #되나 안되나 확인해봄 당연히 되겠지만
soup = BeautifulSoup(html,'html.parser')
# print('soup',type(soup)) #클래스로구나
# print('prettyfy',soup.prettify())#이쁘게 출력됨
#근데 걍 html로 처리해서 보는게 빠름

h1 = soup.html.body.h1
print('h1',h1)
# print('h1',type(h1)) #클래스임을 알수있다
# print(h1.string) #문자열만 출력

p1 = soup.html.body.p
print('p1',p1)

p2 = p1.next_sibling.next_sibling #p1에서 이동도 가능한가봄 아무것도 안가져왔다=줄바꿈을 가져옴 그래서 두번써야됨 지금은
print("p2",p2)

p3= p1.previous_sibling.previous_sibling #이전으로 이동
print("p3",p3)
#직접 접근도 가능하고 이동해서 접근도 가능함

print("h1>> ",h1.string)
print("h1>> ",p1.string)
print("h1>> ",p2.string)
#정확하게 출력이 가능하다
#시블링은 잘 쓰지는 않는다 왜냐면 디자인이 조금만 달라져도 잘못된 정보를 가져오므로 비동기적이므로
