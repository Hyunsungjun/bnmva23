class SelfTest:
    def function1(): #def 빨간줄 왜 안없어져
        print("function1 called!")
    def function2(self):
        print("function2 called!")
        print(id(self))

f = SelfTest()
print(dir(f)) #명령어 보는거같은데?

# f.function1()
print(id(f))
f.function2()
print(SelfTest.function1())#아규먼트로는 불러올수 있다나봄

#파이썬 클래스 메소드 호출은 .인자() 호출하는것과 f = selftest()처럼 부르는것 두가지 
