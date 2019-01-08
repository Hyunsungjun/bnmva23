from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep #분석을 해보면 한글url이 들어가니 이것도 해주세용
import os
# import io
# import sys


#3vs 구글링해서 읽으세요 
# Voulume 데이터의 양
# Variety 데이터의 다양성
# Velocity 데이터의 속도

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아이유")
url = base+quote
# print(url) #잘 출력되나 확인
res = req.urlopen(url)
savePath = "/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/imagedown/"
#예외처리를 해야할 필요가 있어요 폴더만들기 패턴
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res,"html.parser")
#이부분이 어렵게 느껴진다
img_list = soup.select("div.img_area._item > a.thumb._thumb > img") #띄어쓰기에서 .만 되네요
# print("test",img_list)

for i, img_list in enumerate(img_list,1):
    # print(img_list['data-source'])#오.. 
    #파일 이름 주기 패스에 우리 숫자 str선언하고 i는 숫자에 스트링+스트링(jpg)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    print(fullFileName)
    req.urlretrieve(img_list['data-source'],fullFileName)
print("다운로드 완료")

