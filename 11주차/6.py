man_num = int(input('인원수를 입력해주세요:'))
count = int(input('인원 당 구매할 키트 수 를 입력해주세요:'))

total = man_num*count*6000
if count > 5:
    print('인원당 키트 구매 가능 수는 5개까지 입니다. 다시 입력해주세요. ')
else:
    print('총금액은 ', total, "원 입니다.")