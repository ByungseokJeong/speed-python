clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
clovers[1] = '하트2'
print(clovers[1]) # 리스트의 값으로 연결하는 인덱스


clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
del clovers[1]
print(clovers) # 리스트에서 값을 제거하는 del


candies = ['딸기맛', '레몬맛', '수박맛', '박하맛']
print(candies)
candies.append('콜라맛')
print(candies)
del candies[3]
print(candies) # append와 del을 이용한 리스트의 추가와 제거


week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5]) # 리스트에서 여러 값을 가져오는 슬라이싱(원본은 그대로)


candies = ['딸기맛', '레몬맛', '수박맛', '우유맛', '콜라맛', '포도맛']
cat_candy = candies[0]
print('체셔고양이에게는', cat_candy, '사탕을 줘요')
dodo_candies = candies[3:6]
print('도도새에게는', dodo_candies, '사탕을 줘요.') # ,를 사용한 문자열 출력


animals = ['체서고양이', '오리', '도도새']
animals.sort()
print(animals) # 리스트의 문자열을 정렬하는 sort 기능
card = ['하트', '클로버', '하트', '다이아']
print(card.count('하트')) # 리스트 내에서 개수를 세는 count 기능

