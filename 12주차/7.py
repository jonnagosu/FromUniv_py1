x = int(input('숫자를 입력하세요 ->'))
max = x

for n in range(1,5):
    x = int(input('숫자를 입력하세요 ->'))
    if x > max :
        max = x


print(f'최댓값은 {max}')