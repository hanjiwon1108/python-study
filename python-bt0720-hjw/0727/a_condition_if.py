#
# (교과서) if문: 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요.
# 관계 연산자, 논리 연산자
# num = int(input('임의의 정수 3개를 입력하세요(예: 123) : '))
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
#
# if a > b and c:
#     print('a')
# elif b > a and c:
#     print('b')
# elif c > a and b:
#     print('c')
# else:
#     print('세 정수는 같은 수 입니다.')

num1 = int(input('첫 번째 숫자를 입력하세요 : '))
num2 = int(input('두 번째 숫자를 입력하세요 : '))
num3 = int(input('세 번째 숫자를 입력하세요 : '))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print('가장 큰 수는', largest, '입니다.')






# 2.
# (교과서) if문: 미세먼지 저감 활동의 힐환으로 차량 2부제를 실시하고자 합니다.
# 사용자로부터 차량번호를 입력받아 차량번호가 짝수로 끝나면 '운행가능'
# , 아니면 '운행불가'를 출력하는 프로그램을 구현하세요.
# 단, 차량번호는 '237가 1234'와 같은 형식으로 입력 받는다고 가정합니다.

car_number = input('차량 번호를 입력하세요(예: 123가 4567) : ')

# 입력 받은 차량 번호에서 마지막 숫자를 추출
last_digit = int(car_number[-1]) # '4' -> 4

# 마지막 숫자가 짝수인지 홀수인지 판별
if last_digit % 2 == 0:
    print('운행 가능')
else:
    print('운행 불가')