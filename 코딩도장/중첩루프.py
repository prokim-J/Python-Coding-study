#계단식으로 별 출력하기
#for i in range(1, 6): # 바깥쪽 루프
#    for j in range(i): #안쪽 루프
#        print("*", end='')
#    print('')

#for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
#    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
#        print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
#    print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
                                     # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                                     # (print는 기본적으로 출력 후 다음 줄로 넘

#사각형으로 별 출력하기
#for i in range(1, 6):
#    for j in range(5):
#        print("*", end='')
#    print('')

#사각형 모양 바꾸기
#for i in range(0, 3):
#    for j in range(7):
#        print("*", end='')
#    print('')

#대각선으로 별 출력하기
#for i in range(5):
#    for j in range(5):
#        if j == i:
#            print("*", end='')
#        else:
#            print(' ', end='')
#   print() # (print는 출력 후 기본적으로 다음 줄로 넘어감)

#역삼각형 모양으로 별 출력하기
#for i in range(5):
#    for j in range(5):
#        if j < i:
#            print(" ", end='')
#        else:
#            print('*', end='')
#    print()

#임의의 수를 입력하여 (*)별 로 산모양 만들기.
a = int(input())

for i in range(a):
    for j in reversed(range(a)): #reversed 거꾸로 함수.
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
            
    for j in range(a):
        if i > j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
