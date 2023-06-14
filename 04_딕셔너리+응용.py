# 딕셔너리 응용

## 딕셔너리 조작
x = {
    'a' : 10, 'b': 20, 'C': 30
}
print(x)
x['a'] = 100
print(x)

# 객체.메소드(..)
x.update(a=1000)
print(x)
# 2개 이상의 키를 넣을 수 있음
x.update(a = 10, b = 70)
print(x)


# 딕셔너리 키-값 쌍의 삭제
print(x)
del x['a'] # del
print(x)
#print(x.pop())
print(x.pop('b')) # pop은 반환값이 있다.
print(x)
#print(x.pop('hello')) # error
print(x.pop('hello',0)) # 기본값이 0이 나온다.

# x.clear() # 전체 삭제
print(x)


x = {
    'a' : 10, 'b': 20, 'C': 30
}
# get을 통한 값 가져오기
if 'e' in x:
    print(x['e'])
print(x.get("e")) # None
print(x.get("a"))
print(x.get("e", 0))

# 딕셔너리 키-값-아이템
for i in x:
    print(i)

print(x.keys()) # 딕셔너리의 key 목록을 받는 메소드
print(x.values()) # 딕셔너리의 value
print(x.items()) # 딕셔너리의 key, value
for i in x.items():
    print(i)
for k, v in x.items():
    print(f"키 : {k}, 값 : {v}")

######
a = {}
a['b'] = {}
a['b']['c'] = {}
print(a)
a['b']['a'] = 100
print(a)

b = a
print(f"b is a : {b is a}")
a['b']['b'] = 100
print(b)

import copy
d = copy.deepcopy(a)
print(f"d is a : {d is a}")
a['b']['b'] = 1000
print(a)
print(d)

