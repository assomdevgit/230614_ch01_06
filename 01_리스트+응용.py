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

l3 = []
for v1 in l:
    l3.append(v1 * 2)
for v2 in l2:
    l3.append(v2 * 2)
print(l3)












