# for 반복문으로 Hello, world! 100번 출력하기
#a=0
#for i in range(1, 101):
#    a = a+1
#    print("%d Hello, world!" %a)
# 파이썬의 for 반복문은 range에서 in으로 숫자를 하나하나 꺼내서 반복하는 방식임
# range에 횟수만 지정하면 숫자가 0부터 시작하지만, 다음과 같이 시작하는 숫자와
# 끝나는 숫자를 지정해서 반복할 수도 있음

#for i in range(101): #0 ~ 100 번 반복
#for i in range(1, 101): #1 ~ 100 번 반복

# range는 증가폭을 지정해서 해당 값만큼 숫자를 증가시킬 수 있음
#for i in range(1, 101, 2):
#    print("안녕 정석아", i) # 홀수개 99개까지 출력

# range 숫자를 감소시키기.
#for i in range(10, 1, -1):
#    print(i)

# 증가폭을 음수로 지정하는 법 말고도 reversed 함수를 사용하면
# 숫자의 순서를 반대로 뒤집을 수 있음
#for i in reversed(range(10)):
#    print(i)
#for i in reversed(range(1, 10)):
#    print(i)

# 입력한 횟수대로 반복하기
#a = int(input())
#for i in range(a):
#    print(i)

#-----------------------------------------------------------------
#시퀀스 객체로 반복하기
#for에 range 대신 시퀀스 객체를 넣어도 됨
#for는 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있음
#for에 range 대신 리스트를 넣으면 리스트의 요소를 꺼내면서 반복함
#a = [10,20,30,40,50]
#for i in a:
#    print(i)

#튜플도 마찬가지로 튜플의 요소를 꺼내면서 반복함
#a = ('김정석', '아이린', '아이유', '카리나')
#for i in a:
#    print(i)

#한글자한글자 분리해서 출력 하기
#for letter in 'python':
#    print(letter, end=' ')

#문자열 'python' 뒤집어서 문자를 출력하기
#for letter in reversed('python'):
#    print(letter, end=' ')

#for 반복문은 반복 개수가 정해져 있을 때 주로 사용함
#for 반복문은 range 이외에도 시퀀스 객체를 사용할 수 있다는 점이 중요함

#리스트의 요소에 10을 곱해서 출력하기
#x = [49, -17, 25, 102, 8, 62, 21]

#for i in x:
#    print(i * 10, end=' ')

#for 문 이용해서 구구단 출력
gugudan = int(input())

for j in range(1, 10):
    s = gugudan * j
    print("%d * %d = %d"%(gugudan, j, s))