# 연산자 복습 문제 #

# 1. 임의의 두 자리 정수(10 ~ 99)를 입력받아서
# 십의 자리와 일의 자리로 분리하여 출력하는 프로그램을 구현

number = int(input('두 자리 정수를 입력해주세요(10 ~ 99) : ' ))
tens = number // 10
ones = number % 10
print('십의 자리 : ', tens)
print('일의 자리 : ', ones)

# 2. 임의의 세 자리 정수(100 ~ 999)를 입력받아서
# 백의 자리, 십의 자리, 일의 자리로 분리하여 출력하는 프로그램을 작성하세요
number = int(input('세 자리 정수를 입력해주세요(100 ~ 999) : '))
a = number // 100
b = (number % 100) // 10
c = number % 10
print('백의 자리 : ', a)
print('십의 자리 : ', b)
print('일의 자리 : ', c)

# 3. 1분은 60초이고, 1시간은 60분입니다. 따라서 1시간은 3600초 입니다
# 임의의 초를 입력받아 해당 초를 시, 분, 초로 변환하여 출력하는 프로그램을 구현해주세요
total_seconds = int(input('임의의 초를 입력해주세요 : '))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print('시 : ', hours)
print('분 : ', minutes)
print('초 : ', seconds)