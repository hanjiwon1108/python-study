# 연산자(operator)
# : 특정 작업을 수행하는데 사용되는 특수 기호나 구문

# 항목의 개수: 단항, 이항, 삼항 연산자로 구분
# 사용 목적: 산술, 대입, 관계 논리 연산자로 구분

# 파일(폴더)명 변경 단축기: shift + f6

### 산술 연산자 ###
# 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# 모듈로(%), 제곱(**), 몫(//)

a = 5
b = 3
print(a + b) # 덧셈: 8
print(a - b) # 뺄셈: 2
print(a * b) # 곱셈: 15
print(a / b) # 나눗셈 : 5/3 == 1.666666666666666666666666...
print(a % b) # 모듈로(어떤 한 숫자를 다른 숫자로 나눈 나머지를 구하는 연산): 2
print(a ** b) # 제곱: 5 * 5 * 5 == 125
print(a // b) # 몫: 1

### 비교 연산자 ###
# 결과 값이 boolean타입으로 반환
# 두 값이 같은지(==), 두 값이 같지 않은지(!=)
# 이상(>=), 이하(<=), 초과(>), 미만(<)

a = 10
b = 20
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

### 할당 연산자 ###
# : 변수에 값을 할당하는데 사용
# 기본 할당 연산자: 등호(=)
# 복합 할당 연산자: +=, -=, *=, /=, %=, **=, //=

a = 10 # 10을 a에 할당

a += 5 # a = a + 5와 동일 (a의 값: 15)
a -= 2 # a = a - 2와 동일 (a의 값: 13)
a *= 2 # a = a * 2와 동일 (a의 값: 26)
a /= 2 # a = a / 2와 동일 (a의 값: 13.0)

print(a)

### 논리 연산자 ###
# : boolean 값(True, False)을 다루는 연산자
# : and, or, not

a = True
b = False

print(a and b) # False
# : and 연산자는 모든 조건이 True일 때 True를 변환
# : 그렇지 않으면 False를 반환

print(a or b) # True
# : or 연산자는 적어도 하나의 조건이 True일 때 True를 반환
# : 모든 조건이 False일 때만 False를 반환

print(not a) # False
# not 연산자는 boolean 값을 반전

print('==================================================')
a = 10
b = 5
c = a + b
print(c) # O

d = 7
d += 3
print(d) # O

e = 12
f = 9
print(e >= 10 and f >= 10) # O

g = True
print(not g) # O












