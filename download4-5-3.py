#numpy 예제  

import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성 
# df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(100,4), columns=['ONE','TWO','THREE','FOUR'])
print(df)
#randint 랜덤int 0부터 100까지 100개rows 4개 coulmn
df.to_csv('/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/result_s2.csv',index=False,header=False)

# 과제 : https://support.spatialkey.com/spatialkey-sample-csv-data/
# CSV: https://ko.wikipedia.org/wiki/CSV_(%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D)
# Pandas: http://pandas.pydata.org/