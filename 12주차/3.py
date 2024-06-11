sum = 0
a = 1

for a in range (200, 1000+1):
    if a%2==0:
        sum = sum + a

print(f'정수 200부터 1000사이의 짝수들의 합은 {sum}입니다.')
