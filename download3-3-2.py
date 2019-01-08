#Rest API 에서 원하는 데이터를 받아와서 앱을 만듦 
#http uri로 Resource 위치를 명시하고 Method: 명시
#get post put(fetch) delete 등을 하고 
#Rest : POST, GET(가져오는것), PUT:업뎃,리플레이스(FETCH:업뎃,모디파이), DELETE
import requests ,json

payload1 = {'key1':'value1','key2':'value2'}#dict
payload2 = (('key1','value1'),('key2','value2'))#튜플
payload3 = {'some':'nice'}

# r = requests.put('http://httpbin.org/put',data=payload1)
# print(r.text)

# r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
# print(r.text)#플라스크로 테스트 

# r = requests.delete('https://jsonplaceholder.typicode.com/posts/1') #첫 포스트 글을 지워라 
# print(r.text)

#정리 
#리퀘스트 모듈 사용법, rest api 실습해봄 put get delete 실습 