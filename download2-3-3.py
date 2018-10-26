import urllib.request as req
from urllib.parse import urlencode

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
values = {
    'ctxCd':'1001'
}
print('before',values)
params = urlencode(values)#api를 쓸수있게 동적으로 고치기
print('after',params)

url = API + "?" + params
print('요청 url',url) #확인 api가 요구한 형식을 동적으로 바궈주엇다

reqData = req.urlopen(url).read().decode('utf-8')
print('출력',reqData)# 완성