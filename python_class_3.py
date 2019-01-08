#클래스 변수 , 인스턴스 변수 알아보자 

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name) #공유안됌 
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)#인스턴스 네임스페이스 -> 클래스 네임스페이스를 찾음 -> 에러발생
#클래스 변수는 공유가 된다 
print(user1.stock_num) #클래스변수는 공유가됌
print(user2.stock_num)