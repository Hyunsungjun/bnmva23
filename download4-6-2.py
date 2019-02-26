#액셀 
import pandas as pd

df = pd.read_excel('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/excel_s1.xlsx', header=0)
# print(df)

#컬럼 값 수정 
# print(df['State']) #컬럼 값 가져오기 
# df['State'] = df['State'].str.replace(' ','|')
# print(df)

#평균 컬럼 추가 
df['Avg'] = df[['2003','2004','2005']].mean(axis=1)
print(df)