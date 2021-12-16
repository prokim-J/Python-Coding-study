#while 반복문으로 Hello, world! 100번 출력하기
#i = 0
#while i < 100:
#    i = i + 1
#    print("Hello, world!", i)

# while 반복문은 조건식으로만 동작하며 반복할 코드 안에
# 조건식에 영향을 주는 변화식이 들어감
# 조건식을 판별하여 참(Ture)이면 코드를 계속 반복하고, 거짓(False)이면
# 반복문을 끝낸 뒤 다음 코드를 실행함
# while 다음 줄에 오는 코드는 반드시 들여쓰기를 해줌

#초깃값을 감소시키기
#i = 10
#while i > 0:
#    i = i - 1
#    print(i)

#입력한 횟수대로 반복하기
#x = int(input())
#i = 0
#while i < x:
#    i = i + 1
#    print(i) 

#반복 횟수가 정해지지 않은 경우
# 난수를 생성해서 숫자에 따라 반복을 끝내보자
# 난수(random number)란 특정 주기로 반복되지 않으며
# 규칙 없이 무작위로 나열되는 숫자를 뜻함
# 현실에서 쉽게 접할 수 있는 난수가 바로 주사위를 굴려서 나온 숫자임

# 랜덤 함수 써서 랜덤한 숫자 가져오기
#import random # random 모듈을 가져옴
#print(random.random())

# randint 함수는 난수를 생성할 범위를 지정함
#import random
#print(random.randint(1, 11)) #1~10 까지의 난수가 생성됨.

#문제 = 1과 6사이의 난수를 생성한 뒤 3이 나오면 반복을 끝냄
#import random
#i = 0
#count = 0
#while i != 3:
#    count = count + 1
#    i = random.randint(1, 6)
#    print("(%d) %d 번 반복했습니다."%(i,count))

#while 반복문으로 무한 루프 만들기
#while True:
#   print("Hi")

#무한루프에 빠졌을때 강제로 끝내는 방법은 Ctrl+C를 입력하려 무한루프 종료.

#변수 두 개를 다르게 반복하기
#i = 2
#j = 5

#while i < 33 or j > 1:
#    print(i, j)
#    i = i * 2
#    j = j - 1

#교통카드 잔액 출력하기
#money = int(input())

#while money > 0:
#    money = money - 1350

#    print(money)
#    if money < 1350:
#        break