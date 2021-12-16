#elif를 사용하여 여러 방향으로 분기하기
# if else와 마찬가지로 조건식 끝에 :(콜론)을 붙여야 하고
# elif 단독으로 사용할 수 없음
#x = int(input())
#if x == 10:
#    print("10입니다.")
#elif x == 20:
#    print("20입니다.")
#else:
#    print("모르겠습니다 ㅋ")

#교통카드 시스템 만들기
age = int(input())
balance = 9000    # 교통카드 잔액

if age >= 7 and age <= 12:
    balance = balance - 650
elif age >= 13 and age <= 18:
    balance = balance - 1050
elif age >= 19:
    balance = balance - 1250
    
print(balance)