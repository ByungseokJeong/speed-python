for num in [0, 1, 2]:
    print(num)
characters = ['앨리스', '도도새', '3월토끼']

for character in characters:
    print(character)
players = ['공작부인', '흰 토끼', '하트잭', '모자장수']

for player in players:
    print(player, '퇴장!') # for 변수 in 리스트: 를 사용한 반복실행

for letter in '체셔고양이':
    print(letter) # for i를 사용한 문자열 반복


nums = [0, 1, 2]
for num in nums:
    print(num) 
print(nums) # 맨  마지막에 출력

nums = [0, 1, 2]
for num in nums:
    print(num) 
    print(nums) # 코드블럭 영향범위 내이므로 같이 반복됨
    
for num in range(3): 
    print(num)

for y in range(1, 10):
    print(2, 'x', y, '=', 2 * y) # range를 사용한 숫자열

roses = ['하얀장미', '하얀장미', '하얀장미']
for i in range(3):
    roses[i] = '빨간 장미'
print(roses)
    






    
