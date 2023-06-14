# 리스트

## 리스트 조작하기

### 리스트에 요소 추가하기
'''
* append : 요소 하나를 추가
* extend : 리스트를 연결하여 확장
* insert : 특정한 인덱스에 요소를 추가
'''

### 기존 리스트에 요소 하나 추가하기

a = [10, 20, 30]
print(a)
# a = [10, 20, 30, 500]
a.append(500)
# ? : 없던 인덱스에는 값을 할당할 수 X --> append를 사용하게 되면 신규 인덱스를 생성 및 값 할당
print(a)

# b = []
b = list()
print(b)
b.append(100)
print(b)

### 리스트 안에 리스트 추가하기
l = [[0] * 5] * 5 # 행 -> 열
print(l, len(l))
l.append([1])
print(l, len(l))

### 리스트 확장하기
a = ["사과"]
b = ["배"]
print (a, b)
a = ["사과"] * 3
print(a * 3)
a.extend(b)
# inplace -> 대체 -> 메소드를 실행하는 순간 궅이 재대입/재할당 -> 원래 변수에 영향을 미친다.
print(a)
print(a + b)
# extend => + 가 아니라 += 의 역할을 한다
# exdtend 는 전달받은 리스트의 원소를 하나씩 반복하면서 append라고 보시면 됨.

l = [1, 2, 3]
l2 = [4, 5, 6]
# 1.
l3 = l + l2
print(l3)

# 2.
l3 = []
l3.extend(l)
l3.extend(l2)
print(l3)

# 3.
l3 = []
for v1 in l:
    l3.append(v1)
for v2 in l2:
    l3.append(v2)
print(l3)

# 3-1.
l3 = []
for v1 in l:
    l3.append(v1 * 2)
for v2 in l2:
    l3.append(v2 * 2)
print(l3)

### 리스트의 특정 인덱스에 요소 추가하기
# 리스트객체. insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가한다.
a = list(range(10, 40, 10))
print(a)

a.insert(2, 15) # 순서상 2번째 자리
print(a)
'''
insert(0, 요소): 리스트의 맨 처음에 요소를 추가
insert(len(리스트), 요소): 리스트 끝에 요소를 추가
'''
a.insert(0, 5) # 파이썬 상 속도를 많이 잡아먹음. --> stack, queue, deque. (자료구조)
a.insert(len(a), 5) # a.append(5)
print(a)

### 리스트에서 요소 삭제하기
print("삭제 전", a)
del a[0]
print("삭제 후", a)

store = [1000, 2000, 5162]
# print(store[-1])
# del store[-1]
p = store.pop() # 마지막 값을 삭제

p = store.pop(0)
# 리스트 객체.pop(인덱스) : 해당 인덱스의 값을 꺼내옴.
print(p)
print(store)

# pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제

# 리스트에서 특정 값을 찾아서 삭제
cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키']
print(cookies)
cookies.remove("치즈 쿠키") # pop 처럼 삭제된 결과 X
# 특정한 값을 찾는 기능.
print(cookies)

print(cookies.index("오레오 쿠키"))

# idx = cookies.index("오레오 쿠키")
# del cookies[idx]
#
# cookies.remove("오레오 쿠기")
cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '오레오 쿠키']
print("cookies", cookies.index("오레오 쿠키"))

# print(cookies.index("초코파이")) # 오류 발생 ValueError: '초코파이' is not in list
print('초코파이' in cookies) # ValueError: '초코파이' is not in list

# store = ["마제소바", "토리동", "부타동"]
# while store:
#     order = input("order :")
#     if order in store:
#         store.remove(order)
#         print(order + "을(를) 드리겠습니다")
#     else:
#         print(order + "은(는) 현재 없는 메뉴입니다")
#     print("장사 끝났습니다")
#
#
# store = ["마제소바", "토리동", "부타동"]
# # while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
# while True:
#     print(store)
#     order = input("무엇을 주문하시겠습니까? : ")
#     if order in store:
#         store.remove(order)  # 요소를 계속 제거...
#         print(order + "을(를) 드리겠습니다")
#     else:
#         print(order + "은(는) 현재 없는 메뉴입니다")
#     if len(store) == 0: # if not store:
#         break
# print("장사 끝났습니다")

### 특정 값의 개수 구하기

cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '오레오 쿠키', '치즈 쿠키', '치즈 쿠키']
# 쿠키의 개수
print('cookies.count("치즈 쿠키")', cookies.count("치즈 쿠키"))  # 정확하게 일치하는지
song = "'마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키'"
print(song.count("쿠키"))  # 문자열(string) -> 특정한 단어가 몇 개 존재하는지?

### 리스트 뒤집기
print(cookies)
print(cookies[::-1])
print(list(reversed(cookies)))
cookies.reverse()
print(cookies)

### 리스트의 요소 정렬
'''
sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
'''
import random
r_number = random.choices(range(1000), k=10)
print(r_number)

print(sorted(r_number))
print(sorted(r_number, reverse=True))
print(list(reversed(sorted(r_number))))


r_number.sort()
print("r_number.sort()", r_number)
print(r_number)
r_number.sort(reverse=True)
print("r_number.sort(reverse=True)", r_number)

print("cookies", cookies)
cookies.clear()
print("cookies", cookies)

### 리스트의 할당과 복사
'''
어떠한 값을 새로운 곳에 복사하는 방법
1. 할당 (assignment)
2. 얕은 복사 (shallow copy)
3. 깊은 복사 (deep copy)
'''
a = [0] * 5
print("a", a)
b = a
print("b", b)
a[0] = 100
a[1] = 150
print("b", b)
print("a is b", a is b)

c = a[:] # 슬라이스로 복사한 경우에는 할당이 아니라 앝은 복사' 이므로 서로 영향을 미치지 X
print("a is c:", a is c)
a[0] = 1200
a[1] = 1500
print("c", c)

d = a.copy() # 얕은 복사
print("c is d", c is d)

e = [a, b, c] # 리스트를 담은 리스트
f = e.copy()
print("e is f", e is f)
print(f)
a[0] = 1338
print(f)

import copy
g = copy.deepcopy(e)
print("g", g)
print("g is e", g is e)

# 1. 할당 - 얕은 복사 : 할당 -> 특정한 데이터를 저장한 주소를 넘기는 것.
# 2. 얕은 복사 -> 같은 데이터지만, 다른 주소를 가지도록 사본을 만드는
# (내부에 들어있는 주소까지 연결을 끊어주진않아요)
# 3. 깊은 복사 (import copy.deepcopy) -> 모든 주소들의 연결을 끊어버려서 사본을 만드는 것.


# 리스트(튜플) 가장 작은 수, 가장 큰 수, 합계
# 가장 작은 수, 가장 큰 수

# 1. 정렬
a = random.choices(range(1, 1000), k=4)
print("a", a)
a.sort()
print("a", a)
print("최소값", a[0])
print("최대값", a[-1])

# 2. 반복
b = random.choices(range(1, 1000), k=10)
n = 0
for v in b:
    if n < v:
        n = v # 더 큰 값을 n에 대입해서...
print(b, n)

# 3. 함수
# 최대값 : maximum
# 최소값 : minimum
print(max(b))
print(min(b))

# 합계
s = 0
for i in range(1,10):
    s += i
print(s)

# summerization
print(sum(range(1,10)))
print(sum([333,232,231]))

# 문자열들은 sum을 쓸 수 없다.

# 리스트 표현식 (list comprehension)
## -> 리스트 안에 for 반복문과 if 조건문으로 -> 값들의 묶음을 표현.
## -> 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성 = 리스트 컴프리헨션
## [식 for 변수 in 시퀀스]

a = []
for i in range(10):
    a.append(i ** 2)
print(a)

a = [i ** 2 for i in range(10)]
print(a)
a = [i ** 0.5 for i in range(10)]
print(a)

b = ["아메리카노", "카푸치노", "프라푸치노"]
c = []
for v in b:
    c.append(v[-2:])
print(c)
c = [v[-2:] for v in b]
print(c)
c = [v + " 나왔습니다." for v in b]
print(c)

# 리스트 컴프리핸션 + if 조건문
'''
[식 for 변수명 in 리스트 if 조건식]
'''
d = []
for v in b:
    #print(v)
    if "푸" in v:
        # print(v)
        d.append(v)
print("d", d)
e = [v for v in b if "푸" in v]
print("e", e)

# 조건부 표현식 (삼항연산자) -> for 앞에 (식)
e = ["나 단거 좋아해" if v == "프라푸치노" else "나 단거 싫어해" for v in b if "푸" in v]
print(e)
# 리스트 컴프리헨션의 if문은 -> 만족을 안 시키면 필터링. -> continue -> len이 바뀜 !!!!
# else가 없음...
# 조건부 표현식(삼항연산자)는 조건의 T/F와는 상관없이 각 행이 여전히 존재. => 값. -> len 안바뀜
# else가 있음...

# 이중 for문
for i in range(10):
    for j in range(10):
        print(i, j, i * j)

## 이중 for문? 이중 리스트 컴프리핸션
print([(i, j, i * j) for j in range(0, 10,2) for i in range(0, 10,3)])






