#엑셀을 다뤄본다 
import pandas as pd

#xlrd, opnepyxL 사용하기 

#기본 읽기1 

# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx')#시트이름을 불러올수 있다 디폴트는 0번임 
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', sheet_name=0)#시트이름을 불러올수 있다 디폴트는 0번임 
# print(df)
# print(df.head())#상위 5개
# print(df.tail())#하위 5개

#행,푸터(Footer) 스킵
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', skiprows=[0])#첫번째것 스킵함 
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', skiprows=[0],skip_footer=10)#footer 하위 10개를 스킵하는것
# print(df)

#헤더 정의(1)
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', header=0)#디폴트는0이고  1을두면 값이 헤더가되버림
# print(df)
# print(list(df))#이거랑 아래는 같은거 
# print(list(df.columns.values))

#헤더 정의(2)
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx',skiprows=[0], header=None, names=['State',2003,2004,2005])#헤더를 명시적으로 하는것 위에는 암시적으로 자동으로 잡은것
# print(df)

#특정 값 치환 
# df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx',header=[0],na_values='...',converters={"2003":lambda w: w if w > 60000 else None})#람다식으로 2003년에 6만이상은 표시 나머진 None으로 표시 
# print(df)
# print(pd.isnull(df))#이거쓰면 참트루로 변환시켜서 나옴

# 실습 정리 및 인덱스 재정의 
df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', header=0)
# print(df)
# print(df.rename(index=lambda x:x+1))#1부터 나옴 
# print(df.rename(index=lambda x:x+1).index) 

