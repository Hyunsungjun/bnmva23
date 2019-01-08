import requests

s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)#

print(r.ok)#true

# if ok == True: #이리 쓸수도있음
#     if status_code == 200:

#https://jsonplaceholder.typicode.com 제이손 테스트 사이트 

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text)
# print(r.json())
# print(r.json().keys())
print(r.json().values())#파이썬제공
print(r.encoding)#이거 중요 
print(r.content)#b가붙었다 binery데이터로 가져옴
print(r.raw)#<urllib3.response.HTTPResponse object at 0x107d3dd68> 
