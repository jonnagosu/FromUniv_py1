coffee = int(input('커피 갯수를 입력해주세요.'))
tea = int(input('티 갯수를 입력해주세요.'))
bread = int(input('빵 갯수를 입력해주세요.'))

coffee_c = (1500 * coffee)
tea_c = (tea*1000)
bread_c = (bread*1500)
total = (coffee_c + tea_c + bread_c)

print('커피 :' , coffee ,'/', '차 :', tea ,'/', '빵 :' , bread ,'/', end="")
print('총 금액은', total , '원입니다.')

