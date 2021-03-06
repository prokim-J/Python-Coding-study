#시퀀스 자료형 활용하기
#값이 연속적으로 이어진 자료형을 시퀀스 자료형이라 부름

#시퀀스 자료형 : list, tuple, range, str, bytes, bytearray
#시퀀스 자료형의 특징 : 공통 동작과 기능을 제공
#시퀀스 객체 : 시퀀스 자료형으로 만든 객체
#요소 : 시퀀스 객체에 들어있는 각 값

#리스트 a에서 30과 100이 있는지 확인함
#a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#print(30 in a) #a 안에 30이 있는가? True

#시퀀스 객체에 not in 연산자 : 특정 값이 없는지 확인함
#print(30 not in a) #a 안에 30이 없는가? False

#튜플, range, 문자열도 같은 방법으로 활용 가능
#a = (10,20,30,40,50,60)
#print(40 in a)

#시퀀스 객체 연결하기
# + 연산자로 두 객체를 연결해 새 객체를 만들 수 있음
#a = [0, 10, 20, 30]
#b = [9, 8, 7, 6]
#print(a + b)

#시퀀스 자료형 중에서는 range는 + 연산자로 객체를 연결할 수 없음
#range를 리스트 또는 튜플로 만들어서 연결하면 됨.
#print(list(range(0,10)) + list(range(10, 21)))
#print(tuple(range(0,10)) + tuple(range(10, 21)))

#문자열은 + 연산자로 여러 문자열을 연결할 수 있음
#print("Hello JungSeok" + "Oh ! Hi python")

#시퀀스 객체 반복하기
# * 연산자 : 시퀀스 객체를 특정횟수만큼 반복하여 새 시퀀스 객체를 만듦
# (0 또는 음수를 곱하면 빈 객체가 나오며 실수는 곱할수 없음)
#a = [1,2,3,4,5,6] * 3
#print(a)

# range는 + 연산자로 객체를 연결할 수 없고
# 마찬가지로 range는 * 연산자를 사용하여 반복할 수 없음
# 대신 튜플이나 리스트로 만들어서 반복하면 됨
#a = list(range(0, 10)) * 3
#print(a)
#a = tuple(range(0, 10)) * 3
#print(a)

#----------------------------------------------------------------------
#시퀀스 객체의 요소 개수 구하기.
# 시퀀스 객체에는 요소가 여러 개 들어있는 이 요소의 개수(길이)를 구할 때는 
# len 함수를 사용함.
#a = [1,2,3,4,5,6,7,8,9]
#print(len(a))

#range를 이용한 len 함수 사용하기
#a = len(range(1,10))
#print(a)

#문자열의 길이 구하기
#hello = "hello, world!"
#print(len(hello))

#-----------------------------------------------------------------------
# 인덱스 사용하기
# 인덱스는 항상 0 번부터 시작함.
# 시퀀스 객체의 각요소는 순서가 정해져 있으며, 이 순서를 인덱스라고 부름
# 시퀀스 객체에 [](대괄호)를 붙이고 [] 안에 각 요소의 인덱스를 지정하면
# 해당 요소에 접근할수 있음.

#a=[10,20,30,40,50,60,70]
#print(a[0]) # 첫번째 인덱스 10 출력

# 인덱스(index, 색인)는 위치 값을 뜻하는데 
# 국어사전 옆면에 ㄱ,ㄴ,ㄷ로 표시해 놓은것과 비슷함

# 튜플,range,문자열도 []에 인덱스를 지정하면 해당 요소를 가져올수 있음
#a = range(0, 10 , 3)
#print(a[3])

#문자열은 요소가 문자이므로 인덱스로 접근하면 문자가 나옴
#a = "Hello, JungSeok!"
#print(a[4])

#음수 인덱스 지정하기
#시퀀스 객체에 인덱스를 음수로 지정하면 뒤에서부터 요소에 접근하게됨.
#a = [10, 20, 30 ,40 ,50 ,60]
#print(a[-1]) # 첫번째에서 -1 인덱스 60 출력

#----------------------------------------------------------------------
#슬라이스 사용하기
#시퀀스 슬라이스 : 시퀀스 객체의 일부를 잘라냄
#시퀀스객체[시작인덱스:끝인덱스]
#a = [10,20,30,40,50,60,70]
#print(a[0:5]) # [10,20,30,40,50]

#요소가 10개들어있는 리스트를 처음부터 끝까지 가져오려면 [0:9]가 아닌
#[0:10] 이라야 함

#슬라이스는 a[0:-1]과 같이 음수를 인덱스로 지정할 수도 있음
#print(a[0:-1])

#인덱스 증가폭 사용하기
#슬라이스는 인덱스의 증가폭을 지정하여 범위 내에서 인덱스를 건너뛰며
#요소를 가져올 수 있음
#print(a[0:-1:2])

# 슬라이스를 사용할 때 시작 인덱스와 끝 인덱스를 생략할 수도 있음
# 리스트 a에서 a[:7]과 같이 시작 인덱스를 생략하면 리스트의 처음부터 끝
# 인덱스 - 1(인덱스 6)까지 가져옴
#a = [12,23,34,45,56,67,78]
#print(a[:7]) #[12, 23, 34, 45, 56, 67, 78]
#print(a[0:]) #[12, 23, 34, 45, 56, 67, 78]
#print(a[:]) #[12, 23, 34, 45, 56, 67, 78]
# 생략 : 처음부터 or 끝까지

#인덱스를 생략하면서 증가폭 사용하기
#print(a[:7:2]) #[12, 34, 56, 78]
#print(a[3::2]) #[45, 67]
#print(a[::2]) #[12, 34, 56, 78]

#len() 함수를 응용하여 리스트전체 가져오기
#print(a[0:len(a)]) #[12, 23, 34, 45, 56, 67, 78]

# 파이썬에서는 튜플, range, 문자열도 시퀀스 자료형이므로 
# 리스트와 같은 방식으로 슬라이스를 사용할수 있음.

#range에 슬라이스를 사용하면 지정된 범위의 숫자를 생성하는 range 객체를 새로 만듦
#a = range(0,20)
#b = list(a[4:len(a)]) # 잘라낸 range객체를 리스트로 만들려면 list에 넣으면됨.
#print(b)

# 시퀀스 객체는 슬라이스로 범위를 지정하여 여러 요소에 값을 할당할 수 있음.
# 시퀀스 객체[시작인덱스 : 끝인덱스 ] = 시퀀스객체
#a[2:5] = ['a', 'b', 'c']
#print(a) #[12, 23, 'a', 'b', 'c', 67, 78]
# *범위를 지정해서 요소를 할당했을 경우에는 원래 있던 리스트가 변경되며
# 새리스트는 생성되지않음

# 인덱스 증가폭을 지정하여 인덱스를 건너 뛰면서 할당해보기.
# 인덱스 증가폭을 지정했을때는 슬라이스 범위의 요소 개수와 할당할 요소 개수가
# 정확히 일치해야함.
#a[2:7:2] = ['김', '정', '석']
#print(a) #[12, 23, '김', 45, '정', 67, '석']

# *참고로 튜플,range,문자열은 슬라이스 범위를 지정하더라도 요소를 할당할수 없음

#del함수 로 슬라이스 삭제하기
#del a[2:4]
#print(a) #[12, 23, 56, 67, 78]

#인덱스 증가폭을 이용해서 del함수로 슬라이스 삭제하기
#del a[2:8:2]
#print(a) #[12, 23, 45, 67]

# *참고로 튜플,range,문자열은 del함수로 슬라이스를 삭제할수 없음.

# *코딩도장 퀘스트*
# 표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 
# 리스트 x에 저장됩니다(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음).
# 다음 소스 코드를 완성하여 리스트 x의 마지막 요소 5개를 삭제한 뒤 
# 튜플로 출력되게 만드세요.
#x = input().split()
#del(x[5:len(x)])
#print(tuple(x[:]))

#a = str(input())
#b = str(input())
#print(a[1::2] + b[0::2])

#split() 문자열을 나누어주는 함수.
