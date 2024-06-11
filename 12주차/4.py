x = int(input('숫자를 입력하세요.'))
y = int(input('숫자를 입력하세요.'))
n = 0
sum = 1

for n in range(1, y+1):
    sum = sum*x

print(f'{x}의{y} 제곱은 {sum} 입니다.')