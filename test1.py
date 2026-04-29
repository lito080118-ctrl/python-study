name= input("상품이름")
price=int(input("가격 : "))
quan=int(input("수량 : "))
total = price * quan
print(name, "의 총 금액은 ",total," 원입니다")
print(name+ "의 총 금액은 "+str(total)+" 원입니다")
print(f"{name} 의 총 금액은 {total}")
# print 안에서 f는 f-string이라하며 포맷 문자열
#   ==f" {변수 값}
# 숫자->문자로 변환 :str
# 실수는 float만 있음(8바이트)