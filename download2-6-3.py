from bs4 import BeautifulSoup
#import re #regex http://pythonstudy.xyz/python/article/401-정규-표현식-Regex


fp = open("cars.html")
soup = BeautifulSoup(fp,"html.parser")

#타겟은 그렌져로 잡았음
def car_func(selector):
        print("car_func",soup.select_one(selector).string)


car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")#띄어쓰기 해줘야 오류가없네
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print("car_func",soup.select("li")[3].string)
print("car_func",soup.find_all("li")[3].string)

#람다식
car_lambda = lambda q : print("car_lambda",soup.select_one(q).string)

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")#띄어쓰기 해줘야 오류가없네
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")