#module importing
import urllib.request as ur
#making definition
imgUrl = "https://img.insight.co.kr/static/2017/08/15/700/7t0i8dh5ok7v7mlt652s.jpg"
htmlUrl = "http://google.com"
savePath1="/Users/hyeonseongjun/Desktop/inflearn/test1.jpg"
savePath2="/Users/hyeonseongjun/Desktop/inflearn/index.html"
#using module
ur.urlretrieve(imgUrl, savePath1) #매개변수,경로를 받음
ur.urlretrieve(htmlUrl,savePath2)
print("다운로드완료!")
print("hi")
