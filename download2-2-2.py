#module importing
import urllib.request as dw
#making definition
imgUrl = "https://img.insight.co.kr/static/2017/08/15/700/7t0i8dh5ok7v7mlt652s.jpg"
htmlUrl = "http://google.com"
savePath1="/Users/hyeonseongjun/Desktop/inflearn/test1.jpg"
savePath2="/Users/hyeonseongjun/Desktop/inflearn/index.html"
#using module
f = dw.urlopen(imgUrl).read()
#w : write , r: read a: add
saveFile1 = open(savePath1,'wb') #바이너리를 쓴다
saveFile1.write(f)
saveFile1.close()

print("다운로드완료!")
print('zz')