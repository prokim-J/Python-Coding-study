#print("Hello, world!")

#컴퓨테이셔널 씽킹은 4가지로 되어 있습니다.

#분해: 복잡한 문제를 작은 문제로 나눕니다.
#패턴 인식: 문제 안에서 유사성을 발견합니다.
#추상화: 문제의 핵심에만 집중하고, 부차적인 것은 제외합니다.
#알고리즘: 이렇게 정의한 문제를 해결하는 절차입니다(일반화와 모델링은 여기에 포함됩니다).

# is 는 객체를 비교한다.
# 예) a is b 는 a와b를 비교.

# 단락평가 : 첫번째 값만으로 결과가 확실할 때 두번째 값은 확인(평가)하지 않는
# 방법을 말함.

# and 연산자는 두 값이 모두 참이라야 참이므로 첫 번째 값이 거짓이면 두번째 값은 확인하지
# 않고 바로 거짓으로 결정함
#첫 번째 값이 거짓이므로 두번째 값은 확인하지 않고 거짓으로 결정
#print(False and True) # False
#print(False and False) # False
#print(True and False) # False

# or 연산자는 두 값중 하나만 참이라도 참이므로 첫번째 값이 참이면 두번째 값은 확인하지 않고
# 바로 참으로 결정함
#첫 번째 값이 참이므로 두번째 값은 확인하지 않고 참으로 결정
#print(True or True) # True
#print(True or False) # True
#print(False or True) # true

# 값을 여러개 입력받아 한개 출력하기.
# input 값을 한번에 여러 개를 입력받으려면 함수 input().split() 를 사용하면 된다
# split, input의 결과를 매번 자료형으로 변환해주는게 귀찮을때
# map함수를 사용하면 좋다.
#a,b,c,d = map(int, input().split())
#if a >= 90 and b > 80 and c > 85 and d >= 80:
#    print(True)
#else:
#    print(False)

# 값을 여러개 출력하기
# 값 사이에 공백이아닌 다른 문자 넣기 함수 sep=""
# 값 뒤에 공백이아닌 다른 문자 넣기 함수 end=''

