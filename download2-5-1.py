from urllib.parse import urljoin

baseUrl = "https://test.com/html/a.html" #있다고 가정
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
#나머지만 파싱할수있음 앞에껀 고정되있고
print(">>", urljoin(baseUrl, "../index.html"))
#..이 하나위로 올라가는거니까 올라가게 되는거
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
#다가능하다~










# BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Seletor: https://www.w3schools.com/css_selectors.asp 없어졋네
# 온라인(추천) : https://www.w3schools.com/cssref/trysel.asp