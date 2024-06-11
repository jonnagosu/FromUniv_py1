os = int(input('점수를 입력하세요:'))
db = int(input('점수를 입력하세요:'))
c = int(input('점수를 입력하세요:'))\

sum = (os+db+c)
ave = (sum//3)

if ave>= 90:
    score='A'
else: 
    if ave>= 80:
        score='B'
    else:
        if ave>=70:
            score='C'
        else:
            score='F'
            
print('총점 :', sum, '/', '평균 :', ave, '/', '학점 :', score, '/')