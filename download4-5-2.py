#pandas 

import pandas as pd


#읽기(새로운 파일로) 
df2 = pd.read_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/csv_s2.csv',sep=';', skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])#sep는 구분자이다 
# print(df)

#컬럼 내용 추가 
# df2['Grade'] = df2['Grade'].str.replace('C','A++')
# print(df2)

#평균 컬럼 추가 
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)#여러개는 [[]]로 넣어준다  1은 row행을 나타낸다 mean은 최소값이지만 평균을 나타냄 
# print(df2)

#합계 컬럼 추가 
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)

df2.to_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/result_s1.csv',index=False)