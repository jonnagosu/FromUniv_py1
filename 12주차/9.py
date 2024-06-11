x = int(input('숫자를 입력하세요.'))

for n in range(1, x+1):
    if x % n == 0:
        print(n,",", end="")



print(f'은 {x}의 약수')