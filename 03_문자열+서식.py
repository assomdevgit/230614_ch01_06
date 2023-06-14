# 문자열 서식

# 데이터 -> str(...) print(..., ...., ..)
# 파이썬 3.6 -> f-string

## f-string
'''
문자열 안에 변수의 값들을 삽입하기 위한 양식
'''
name = "박코딩"
age = 30
print("이름 :", name, "나이 :", age, "세")
print("이름 :" + name + "나이:" + str(age))
# f"" or f''
print(f"이름 : {name} 나이 : {age}세")

f = 0.123432345 # 소수점 밑의 2자리
print(f'{f:.2f}')
print(f'{f:.4f}')

# format 메소드 -> 변수에 사용하기에 편하게

