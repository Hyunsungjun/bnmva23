#module importing
import urllib.request as dw
#making definition
imgUrl = "https://img.insight.co.kr/static/2017/08/15/700/7t0i8dh5ok7v7mlt652s.jpg"
htmlUrl = "http://google.com"
savePath1="/Users/hyeonseongjun/Desktop/inflearn/test1.jpg"
savePath2="/Users/hyeonseongjun/Desktop/inflearn/index.html"
#using module
f = dw.urlopen(imgUrl).read() #read로 호출한다
#w : write , r: read a: add
f2 = dw.urlopen(htmlUrl).read()
saveFile1 = open(savePath1,'wb') #바이너리를 쓴다
saveFile1.write(f)
saveFile1.close()


#close()를 자동으로 반납해주는 코드 이코드를 더 강추함
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)


print("다운로드완료!")
print('zz')

#urlretrieve 
# 다이렉트 다운로드 저장 -> open -> 변수에 할당 -> 파싱 -> 저장
#urlopen 이게 좀 더 자주쓰임
# 저장하기 전에 메모리에 변수할당 -> 파싱 -> 저장(db,등등)
# https://wikidocs.net/26
# https://docs.python.org/3/library/urllib.request.html