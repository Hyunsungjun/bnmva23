#pandas 
# FL_insurance_sample.csv

import pandas as pd

#판다스 csv 불러오기
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv')
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/FL_insurance_sample.csv')
# print(df)

#인덱스 0,1 스킵하기 행스킵
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv', skiprows=[0,1])
# print(df)

#헤더 집어넣기 행스킵, 헤더 생략, 해더정의
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015])
# print(df)

#인덱스 컬럼 정의 
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015],index_col=[0])
# print(df)

#특정 값 치환 
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015],index_col=[0], na_values=['JAN'])
# print(pd.isnull(df))
# print(df)

#실습 정리 및 인덱스 재정의 
# df = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015])
# print(df)
# print(df.index) # 0부터 12까지 1계단씩 
# print(list(df.index))#위아래 같음 
# print(df.index.values)#3세개가 같음
# print(df.index.values.tolist())
# print(df.rename(index={0:'aa',1:'bb',2:'cc'})) #dict로 받는데 불편하다 그래서 람다식을 이용 
# print(df.rename(index=lambda x:x*10))

# #읽기(새로운 파일로) 
# df2 = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s2.csv',sep=';', skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])#sep는 구분자이다 
# # print(df)

# #컬럼 내용 추가 
# # df2['Grade'] = df2['Grade'].str.replace('C','A++')
# # print(df2)

# #평균 컬럼 추가 
# df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)#여러개는 [[]]로 넣어준다  1은 row행을 나타낸다 mean은 최소값이지만 평균을 나타냄 
# # print(df2)

# #합계 컬럼 추가 
# df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
# print(df2)