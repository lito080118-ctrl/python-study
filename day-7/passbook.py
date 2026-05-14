class Passbook:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,money):
        self.balance += money
        print(f"(money)원 입금 완료")
        print(f"현재 잔액은 (self.balance)원 입니다")

    def withdraw(self,money):
        if money <= self.balance: #잔액이 출금금액보다는 크거나 같아야함
            self.balance += money
            print(f"(money)원 출금 완료")
            print(f"현재 잔액은 (self.balance)원 입니다")
        else:
            print("잔액 부족")
    def showInfo(self):
        print("예금주: ",self.owner)
        print("현재 잔액: ",self.balance)

class MinusPassbook(Passbook): #상속
     def withdraw(self,money):
        if (self.balance-money) >= -1000000:
            self.balance += money
            print(f"(money)원 출금 완료")
            print(f"현재 잔액은 (self.balance)원 입니다")
        else:
            print("마이너스 한도 잔액 부족")

account1 = Passbook("홍길동",100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2 = MinusPassbook("김철수",100000)
account2.showInfo()
account2.withdraw(120000)
account2.withdraw(9000000)