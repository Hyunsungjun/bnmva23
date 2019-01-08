import requests ,json

s = requests.Session()
r = s.get('http://httpbin.org/stream/20',stream=True)#명시적으로 스트림 기재하는게 더좋습니다
# print(r.text)
# print(r.json()) # 보기엔 제이손인줄 알았으나 에러가 난다 
print(r.encoding) # 유니코드가 None이네? 디코드 하줘야함 

if r.encoding is None: #만약 r이 N이면 urf-8로 하자 
    r.encodning = 'utf-8'

for line in r.iter_lines(decode_unicode=True): #이터레이트 라인 유니코드 에러를 트루로 하겠다 
    # print(line)
    b = json.loads(line) #dict
    # print(type(b))
    # print(b['origin'])
    for e in b.keys():
        print("key:",e,"values:",b[e])#각 json에 대한 모든 값을 호출

#정리 
# 리퀘스트 장점 제이손 데이터 핸들링 리퀘스트모듈 테스트 실습