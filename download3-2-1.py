import requests

s = requests.Session()#세션을 열자
# r =  s.get('https://www.naver.com')#get,post,put(fetch),delete 등을 쓸수있다
# print('1',r.text)
r = s.get('http://httpbin.org/cookies',cookies={'from':'myName'})#테스트하는 사이트
print(r.text) #프롬과 마이네임이 불러져온다
url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}
r = s.get(url,headers=headers)
print(r.text)



s.close()#세션을 열었으니 닫아야지

with requests.Seesion() as s: # 이거쓰면 클로즈 안써도 잘돌아감
    r = s.get('http://www.naver.com/')
    print(r.text)

#요약 쿠기와헤더정보를 겟방식으로 보냈고 확인해보았다