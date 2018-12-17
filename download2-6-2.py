from bs4 import BeautifulSoup
#import re #regex http://pythonstudy.xyz/python/article/401-정규-표현식-Regex


fp = open("food-list.html")
soup = BeautifulSoup(fp,"html.parser")

print("1",soup.select_one("li:nth-of-type(8)").string) #type,child가 있다 8번째 li를 선택하라 같네
print("2",soup.select_one("#ac-list > li:nth-of-type(4)").string)  #자손선택자
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #조건에 맞는 값을 리스트 형태로 반환 한개여도 인덱스로 접근해야함.
print("4",soup.select("#ac-list > li.alcohol.high")[0].string) #
#여기까지 셀렉팅 하는 방법 쉬운거 위주로

param = {"data-lo":"cn","class":"alcohol"}
print("5",soup.find("li",param).string)#이게 가독성은 좋음
#사전을 이용해서도 출력 가능한가봄
print("6",soup.find(id="ac-list").find("li",param).string)#문법을 제대로 이해..

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us',ac.string)
#for 문으로 가져오는것