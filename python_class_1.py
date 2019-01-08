class UserInfo:
    def __init__(self, name, phone):
    # def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-----------")
        print("Name: "+self.name)
        print("Phone: "+self.phone)
        print("-----------")

    def __del__(self): #init이 단한번 실행된다면 del은 메모리 반환 단한번
        print("delete!")

# user1 = UserInfo() #주석한것들 끼리가 완성코드였음
# user2 = UserInfo()

user1 = UserInfo("kim","010-3333-3333")
user2 = UserInfo("kim","010-4444-5555")

print(id(user1))
print(id(user2)) #아이디 값을 함봤어 

# user1.set_info("kim","010-3333-3333")
# user2.set_info("kim","010-4444-5555")

user1.print_info()
user2.print_info() #클래스로 출력 

print(user1.__dict__)
print(user2.__dict__) #dic출력도 가능

print(user1.phone,user1.name) #이렇게도 쓴다 

