arrlist = []

n = int(input('입력 할 숫자의 자릿수를 입력하세요 ->'))
num = int(input('숫자를 입력하세요 ->'))

while(num>0):
    arrlist.append(num%10)
    num=num//10

for item in arrlist:
    print(item, end="")
print('\n 내림차순 정렬')

arrlist.reverse()
print(arrlist, '\n 오름차순 정렬 ')