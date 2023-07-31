
# while문: 사용자로부터 숫자를 계속 입력받다가
# 사용자가 0을 입력하면 프로그램이 종료되는 파이선 프로그램 작성해라.
while True:
    number = int(input('숫자를 입력하세요 (종료하시려면 0을 입력하세요) : '))
    if number == 0:
        break
