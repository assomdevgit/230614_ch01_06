# 문자열

## 문자열 조작하기

### 문자열 바꾸기


'''
문자열.replace('바꿀문자열', '새문자열') -> 기존 문자열 안의 바꿀 문자열을 새 문자열로 '교체'
-> 매번ㄴ 사본이 나옴.
'''

greeting = "안녕하세요! 김파이썬씨"
print(greeting)
print(greeting.replace("파이썬", "코딩"))
print(greeting)

### 문자열 분리하기
### 문자열.split(구분자) -> 구분자를 기준으로 문자열을 리스트화 (구분자를 입력 안하면 -> " " (공백)
a = "태조 정종 태종 세종 문종"
print(a.split(), a.split(" "), a.split("종"))
print(list(a)) # 문자열 -> 리스트 (한 글자씩 쪼개져서 표현)

# map(int, input().split()) # -> 요소요소마다 int를 적용 -> split을 통해서 공백으로 나눠줘서...
a = "태종, 정종, 태종, 세종"
print(a.split(","))

# 문자열 리스트 연결하기 (특정한 구분자를 입력)
b = ['태조', '정종', '태종']
print("".join(b))
print(",".join(b))
print(" ".join(b)) # -> join 빈("")게 가능. / split -> 빈("") 안됨.

# 일괄 대문자화, 소문자화
t = "Hello, Python"
print(t.upper())
print(t.lower())
t = "HELLO! PYTHON"
print(t.isupper())
print(t.islower())

# 채우기 및 삭제
text = "                앞 뒤로 스페이스가 있는 경우               "
print(text)
print(text.replace(" ", ""))
print(text.strip())
print(text.lstrip()) # left
print(text.rstrip()) # right
d = "614" # 4자리 맞춰야함.
print("0" + d)
d2 = "64"
print("00" + d)
print(d.rjust(4,"0")) # 0을 채우기
print(d2.ljust(4,"0"))
# 문자열 왼쪽에 길이를 만족시킬 때까지 0을 넣는...
print(d2.zfill(4))

### 메소드 체이닝
# -> 문자열을 변형시키는 메소드 -> 결과물 문자열 -> 자기 자신에게 계속 변화를 시킬 수 있음.

# 문자열 위치 찾기 & 갯수 세기
# -> 리스트.index(...)
# --> 문자열.find(...)
t = "아메리카노"

## 믄지얄 개수 세기
print(t.count("카"))

