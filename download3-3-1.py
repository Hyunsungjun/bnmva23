#Rest API 에서 원하는 데이터를 받아와서 앱을 만듦 
#http uri로 Resource 위치를 명시하고 Method: 명시
#get post put(fetch) delete 등을 하고 

import requests ,json

# r = requests.get('https://api.github.com/events/')
# r.raise_for_status()#에러가 났을때 예외처리를 해줌
# print(r.text) #json형태로 나오네

#규격화 형식에 맞게 쿠키를 보냄 
jar = requests.cookies.RequestsCookieJar()#왜빨간줄
jar.set('name','kim',domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com',timeout=5)#5초동안 대기
# print(r.text)

#post를 해볼것 본문에 내용이 많을때 데이터를 서버상에 저장하는 형식 
#fake rest 테스트만 성공하면 코드가 성공했다고 보는것 

# r = requests.post('http://httpbin.org/post',data={'name':'kim'},cookies=jar)#delete 등 제공이됨
# print(r.text)

#변수를 선언해서 payload 리퀘스트를 담는다 

payload1 = {'key1':'value1','key2':'value2'}#dict
payload2 = (('key1','value1'),('key2','value2'))#튜플
#json 데이터로 보내기 
payload3 = {'some':'nice'}

# r = requests.post('http://httpbin.org/post',data=payload3)#form데이터
# print(r.text) #1,2든 똑같은 결과값을 나타낸다
r = requests.post('http://httpbin.org/post',data=json.dumps(payload3))#json은 dumps를 쓰면 된다 json데이터 받음
print(r.text) #1,2든 똑같은 결과값을 나타낸다
#증권사는 튜플 데이터로 내리는 경우가 많다고 한다 


