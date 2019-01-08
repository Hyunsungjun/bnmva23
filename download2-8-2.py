from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep #분석을 해보면 한글url이 들어가니 이것도 해주세용
import os
import errno
# import io
# import sys


#3vs 구글링해서 읽으세요 
# Voulume 데이터의 양
# Variety 데이터의 다양성
# Velocity 데이터의 속도

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base+quote
# print(url) #잘 출력되나 확인
res = req.urlopen(url)
savePath = "/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/imagedown/"
#예외처리를 해야할 필요가 있어요 폴더만들기 패턴
try:
    if not (os.path.isdir(savePath)): #경로를 표시
        os.makedirs(os.path.join(savePath)) #폴더 만들기
except OSError as e:
    if e.errno != errno.EEXIST:#파이썬 예외처리 실행은 잘되는데 왜 오류나지
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res,"html.parser") #뷰숩 사용법 읽어봐야할듯

img_list = soup.select("ul.slides")[0]#0번째
# print("test",img_list)

for i, e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.png')
    # print(fullFileName)
    #이미지 태그 확인// src속성 값이므로 src라고 알려줌
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullFileName)
print("다운로드 완료")

