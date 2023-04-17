clovers = '클로버1', '클로버2', '클로버3'
print(clovers)
alice_blue=(240, 248, 255)
r, g, b = alice_blue 
print('R:', r, 'G:', g, 'B:', b) # 언패킹은 list도 가


clover = {'나이':27, '직업': '병사'}
clover['번호'] = 9 # 딕셔너리에 키 값 추가
print(clover)


order = {'스페이드1': '비빔라면', '다이아2': '매운라면'}
print(order)
order['클로버3']  = '카레라면' # 키 '클로버3'와 값 '카레라면' 추가
print(order)
order['다이아2']= '짜장라면' # 키 '다이아2'의 값을 '짜장라면'으로 수정
print(order)
del order['스페이드1'] # 키  스페이드 1 취소
print(order)


def add(num1, num2):\
    return num1 + num2 # add(2,3에 값을 돌려줌)

print(add(2,3))


import random
animals = ['체셔고양이', '오리', '도도새']
print(random.choice(animals)) # 무작위로 출력
print(random.sample(animals, 2)) # 개수를 선택하여 무작위로  출력
import random
print(random.randint(5, 10)) # 정해진 범위중 무작위로 출력

import random
cards = ['하트', '클로버', '스페이드']
chosen_card = random.choice(cards) # 변수 card에서 무작위로 선택후 저장
print(chosen_card, '유죄!')
