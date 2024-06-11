print('팩토리얼 값 구하기.')
x = int(input('숫자를 입력하세요 ->'))
result = 1

for n in range(1, x+1):
    result = result * n

print(f'{x}! = {result}')