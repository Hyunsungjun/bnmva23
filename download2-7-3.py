from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.inflearn.com/%EC%B6%94%EC%B2%9C-%EA%B0%95%EC%A2%8C/"
res = req.urlopen(url).read() #이걸 왜썼는지 다시 공부해서 정리해놓자
soup = BeautifulSoup(res,"html.parser")

# print(soup)

recommand = soup.select("ul.slides")[0]
# print(recommand)

# for e in recommand:#여기서 이너머레이트 추가
#         print(e.select_one("h4.block_title > a").string)

for i,e in enumerate(recommand,1):
        print(i,e.select_one("h4.block_title > a").string)#숫자가 추가되었다.
