import pickle #(객체, 텍스트) 직렬화, 역직렬화 기능을 제공함 

# 파일 이름과 데이터를 선언 
bfilename = '/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/test.bin'
tfilename = '/Users/hyeonseongjun/Desktop/inflearn/section2/test/bnmva23-1/test.txt'

data1 = 77
data2 = 'Hello, world!'
data3 = ["car","apple","house"]

# 바이너리 쓰기
with open(bfilename, 'wb') as f: #롸이트 바이너리 
    pickle.dump(data1,f) #dumps(문자열 직렬화 하는거)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

# 텍스트 쓰기 
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    # f.write(data3) #리스트는 인식을 못해버림 
    f.writelines('\n'.join(data3)) #함수를 지원함 이걸 이용하면 됨

# 바이너리 읽기 
with open(bfilename,'rb') as f: #read binary 
    b = pickle.load(f) #load 역직렬화,객체 불러와서 복원 loads 문자열을 읽어오는것 
    print(type(b),' Binary Read1 | ',b)
    b = pickle.load(f)
    print(type(b),' Binary Read2 | ',b)
    b = pickle.load(f)
    print(type(b),'Binary Read3 | ',b)
    #파이썬은 모든 형태를 자료형으로 인식을함 다시 읽어오더라도 복원을 하는것임 
# <class 'int'>  Binary Read1 |  77
# <class 'str'>  Binary Read2 |  Hello, world!
# <class 'list'> Binary Read3 |  ['car', 'apple', 'house']
# 텍스트는 걍 써짐 string으로 

# 텍스트 읽기 
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line),'Text Read'+str(i)+' | ',line,end='')#끝부분 공백처리 

# <class 'str'> Text Read1 |  77
# <class 'str'> Text Read2 |  Hello, world!
# <class 'str'> Text Read3 |  car
# <class 'str'> Text Read4 |  apple
# <class 'str'> Text Read5 |  house
# 텍스트 저장하고 다시 읽어도 텍스트 
# 데이터 형태 
# XML,JSON,YAML,CSV,EXCEL
# https://docs.microsoft.com/ko-kr/azure/machine-learning/team-data-science-process/prepare-data 
# pickle : https://docs.python.org/3/library/pickle.html
