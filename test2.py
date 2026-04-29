a=2000
b=3000
c=3500
ame= int(input("아메리카노 판매 개수: "))
cafe= int(input("카페라떼 판매 개수: "))
capu= int(input("카푸치노 판매 개수: "))
sales= ame* a
sales= sales + cafe * b
sales= sales + capu * c
print("총 매출은", sales, "입니다.")