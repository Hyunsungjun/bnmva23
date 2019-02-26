# JSON : https://www.w3schools.com/js/js_json_syntax.asp
# SimpleJSON : https://simplejson.readthedocs.io/en/latest/
# JSON Sort 온라인 : https://jsoneditoronline.org/

# JSON의 장점 
# 핸들링이 쉽고 Number, ovject 중첩 , boolean
# string, array, null.. 다 가능 
# 위키도 한번 볼것 


import simplejson as json
# import json #이걸 기반으로 해서 어느걸 껏다 켜도 실행됨 

# Dict(Json)선언 
data = {}
data['people'] = []
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website':'daum.com',
    'from':'Incheon'
})
# 결과 {'people': [{'name': 'Park', 'website': 'google.com', 'from': 'Seoul'}, {'name': 'Kim', 'website': 'naver.com', 'from': 'Busan'}, {'name': 'Lee','website': 'daum.com', 'from': 'Incheon'}]}
# print(data)

# 직렬화, 역직렬화
# dump vs dumps , load vs loads

#Dict(Json) -> Str로 변경 해줘야 되므로 
# e = json.dumps(data)
e = json.dumps(data, indent=4) #indent를 해보니 파일이 생성되었다
# print(type(e))
# print(e)
#str로 전환되었다 이전에는 dict형태였음
# 반대로 str -> dict 하는방법?
d = json.loads(e)
# print(type(d))
# print(d)
#여기까지 dumps vs loads 

with open('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/member.json','w') as outfile:
    outfile.write(e)


#읽어보기 
with open('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/member.json','r') as infile:
    r = json.loads(infile.read())
    print('===')
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name:'+p['name'])
        print('Website:'+p['website'])
        print('From:'+p['from'])
        print('')
1942