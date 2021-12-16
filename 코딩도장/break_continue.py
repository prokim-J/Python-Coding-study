#break, continue로 반복문 제어하기
#break : 제어흐름 중단
#continue : 제어흐름 유지, 코드 실행만 건너뜀

#while문에서 break로 반복문 끝내기
#i = True
#while i:
#   i=i+1
#   print("김정석")
#   if i == 100:
#      break  # break 문 사용법
#break문에는 :(콜론)을 붙이지는 않는다.

#for문 에서 break로 반복문 끝내기
#for i in range(10000):
#    print(i)
#    if i == 100:
#        break

#for에서 continue로 코드 실행 건너뛰기
#for i in range(100): # 0 부터 99 까지 반복
#    if i % 2 == 0:   # i를 2로 나누었을때 나머지가 0일때는
#        continue     # 아래 코드를 실행하지않고 건너뜀.
#    print(i)

#while에서 continue로 코드 실행 건너뛰기
#x = 0
#while x < 100:
#    x = x + 1
#   if x % 2 == 0:
#       continue
#    print(x)

#while문 입력한 횟수대로 반복하기
#a = int(input())
#i = 0
#while True:
#    i = i + 1
#    print(i)
#    if i == a:
#        break

#for문을 이용해 입력한 숫자까지 홀수 출력하기
#a = int(input())

#for i in range(a + 1): # a + 1을 해준이유는 1부터 시작하게 하려구
#    i = i + 1
#    if i % 2 == 0:
#        continue
#    print(i)

#3으로 끝나는 숫자만 출력하기
#for i in range(1, 74):
#    i = i+1
#    if i % 10 == 3:
#        print(i)

#두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
#start, stop = map(int, input().split())
 
#i = start
 
#while True:
#    i += 1
#    if i % 10 == 3:
#        continue
#    if i == stop + 1:
#        break
#    print(i, end=' ')
