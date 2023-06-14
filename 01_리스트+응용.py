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

print(cookies.index("초코파이")) # 오류 발생 ValueError: '초코파이' is not in list
print('초코파이' in cookies) # ValueError: '초코파이' is not in list

store = ["마제소바", "토리동", "부타동"]
while store:
    order = input("order :")
    if order in store:
        store.remove(order)
        print(order + "을(를) 드리겠습니다")
    else:
        print(order + "은(는) 현재 없는 메뉴입니다")
    print("장사 끝났습니다")


store = ["마제소바", "토리동", "부타동"]
# while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
while True:
    print(store)
    order = input("무엇을 주문하시겠습니까? : ")
    if order in store:
        store.remove(order)  # 요소를 계속 제거...
        print(order + "을(를) 드리겠습니다")
    else:
        print(order + "은(는) 현재 없는 메뉴입니다")
    if len(store) == 0: # if not store:
        break
print("장사 끝났습니다")






