#호출한 모듈명과 파일명이 같으면 AttrubuteError가 발생됨

#turtle 그래픽스로 그림 그리기

#import turtle as t
#t.shape('turtle')
#t.fd(100) #forword의 약자 터틀이 앞으로 (100)만큼 가는것을 뜻함
#t.rt(90) #right의 약자 터틀이 오른쪽으로 (90도) 방향을 트는것을 뜻함
#t.fd(100)
#t.rt(90)
#t.fd(100)
#t.rt(90)
#t.fd(100)

#t.mainloop() #터틀창이 바로 닫히는 오류를 t.mainloop() 함수로 막았다

#반복문을 이용해 터틀로 사각형 그림그리기
#import turtle as t
#t.shape('turtle')
#for i in range(4):
#    t.forward(100)
#    t.right(90)

#t.mainloop() 

#반복문을 이용해 터틀로 오각형 그리기
#import turtle as t
#t.shape('turtle')
#for i in range(5):
#    t.forward(100)
#    t.right(360/5)

#t.mainloop() 

#반복문을 이용해 터틀로 다각형 그리기
#import turtle as t

#n = int(input())
#t.shape('turtle')
#for i in range(n):
#    t.forward(100)
#    t.right(360 / n)
#t.mainloop() 

#import turtle as t
 
#n = 6    # 육각형
#t.shape('turtle')
#t.color('black')          # 펜의 색을 빨간색으로 설정
#t.begin_fill()          # 색칠할 영역 시작

#for i in range(n):      # n번 반복
#    t.forward(100)
#    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
#t.end_fill()            # 색칠할 영역 끝

#t.mainloop()

# color에 색깔을 지정할 때 'red', 'green', 'blue', 'yellow',
# 'purple', 'brown', 'gray' 등 영어로 색 이름을 지정합니다.
# 지만 색 이름만으로는 다양한 색상을 표현하기가 힘듭니다.
# 이때는 웹 색상(web color)을 사용하면 됩니다.
# 웹 색상은 #으로 시작하며 빨강(R), 초록(G), 파랑(B)에 
# 해당하는 두 자리 16진수 세 쌍으로 구성되어 있습니다.

#원을 반복해서 그리기
#import turtle as t

#n = 60
#t.shape('turtle')
#t.speed('fastest')
# speed함수
# 'fastest': 0
# 'fast': 10
# 'normal': 6
# 'slow': 3
# 'slowest': 1

#for i in range(n):
#    t.circle(120)
#    t.right(360/n)
#t.mainloop()

#선으로 복잡한 무늬 그리기
#import turtle as t

#t.shape('turtle')
#t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
#for i in range(300):    # 300번 반복
#    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
#    t.right(91)         # 오른쪽으로 91도 회전

#t.mainloop()

# 터틀 모양 설정하기
# 터틀의 shape에는 'arrow', 'turtle', 'circle', 'square',
# 'triangle', 'classic' 등을 지정하여 여러 가지 터틀 모양을 사용할 수 있습니다. 

# 별 그리기

import turtle as t
 
n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360 / n)

t.mainloop()