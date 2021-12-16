#FizzBuzz는 매우 간단한 프로그래밍 문제이며 규칙은 다음과 같습니다.

#1에서 100까지 출력
#3의 배수는 Fizz 출력
#5의 배수는 Buzz 출력
#3과 5의 공배수는 FizzBuzz 출력

#for i in range(1, 101):

#    if i % 3 == 0 and i % 5 == 0:
#        print(" FizzBuzz ", end='')
#    elif i % 3 == 0:
#        print(" Fizz ", end='')
#    elif i % 5 == 0:
#        print(" Buzz ", end='')
#    else:
#        print(" %d "% i, end='')

#-----------------------------------------------------------------------

# 2와 11의 배수, 공배수 처리하기

#1부터 100까지의 숫자를 출력하라
#2의 배수일 때는'Fizz'
#11의 배수일때는 'Buzz'
#2와 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요

#for i in range(1, 101):
    
#    if i % 2 == 0 and i % 11 == 0:
#        print('FizzBuzz')
#    elif i % 2 == 0:
#        print('Fizz')
#    elif i % 11 == 0:
#        print('Buzz')
#    else:
#        print(i)

#--------------------------------------------------------------------

# 5와 7의 배수, 공배수 처리하기

a, b = map(int,input().split())

for i in range(a, b+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)