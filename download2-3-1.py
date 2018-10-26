import urllib.request as req
from urllib.parse import urlparse #이건 다르게
url = "http://www.encar.com/index.do"
mem = req.urlopen(url)

# print(mem) <http.client.HTTPResponse object at 0x1145ee128> 리스폰을 받음
# print(type(mem)) <class 'http.client.HTTPResponse'> 클래스다
# print("getul",mem.geturl()) #주소반환
# print("status",mem.status) #응답코드
# #응답코드 200:정상,404:없다,403:거절,500:서버에러
# print("headers",mem.getheaders())
# print("info",mem.info()) #헤더를 이쁘게
# print("code",mem.getcode()) #status랑 같다
# print("read",mem.read(50)) #리드문으로 범위조정도 가능
# print("read",mem.read(50).decode("utf-8"))
# print(urlparse("http://www.encar.com?test=test"))#정보를 다 스캐닝해준다