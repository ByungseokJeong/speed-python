print(True)
print(False) # 대문자 고정, 약속된 이름
if True:
    print("참") # 조건이 참일 경우 출력
if False:
    print("거짓") # 조건이 거짓일 경우 출력 x
score = 90
if score > 80: # score 90은 80보다 크므로 참 
    print("합격입니다")


total_price = 0
ages = [22, 21, 17, 32, 4, 28, 19, 8]
for age in ages: # ages의 숫자들 반복하여 계산
    if age >=20:
        total_price = total_price + 8000
    elif age >= 10:
        total_price = total_price + 5000
    else:
        total_price = total_price + 2500

print('총 입장료는', total_price, '원입니다.')        


games = 12
points = 25
if games >= 10 and points >= 20: # and가 둘다 true임으로 출력
    print('MVP로 선정되었습니다.')


num = 0
while num < 3: # 조건이 참일 경우 반복
    print('안녕 거북이', num)
    num = num + 1

name = input('이름이 뭔가요? ') #입력값을 호출하는 input 함수
print(name, '안녕!')

# continue = 넘어감   break = 멈춤
# while True : 무한 반복(ctrl c로 해결)



