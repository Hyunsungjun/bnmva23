
class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after: ",NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()
print(id(n1)," vs ",id(n2))
# n1 과 n2 는 공유 되지만 4403865360  vs  4403865472
print(dir())
print(n1.__dict__)
print(n2.__dict__)#나오지 않는다 
n1.total = 77 #값할당 
print(n1.__dict__)#값이 생기니까 {'total': 77} 이리나옴 

print(n1.total)# 77 클래스 영역 안가고 인스턴스값을 출력함
print(n2.total)# 1 클래스에 네임클레스에서 대입해서 1이나옴
# print(n1.next) #없다~ 에러~
