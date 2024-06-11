id_list = []
name_list = []
DB_list = []
PY_list = []
total_list = []
ave_list = []

for n in range(0, 5):
    id_list.append((input('학번을 입력하세요.')))
    name_list.append(input('이름을 입력하세요.'))
    DB_list.append(int(input('DB 점수를 입력하세요.')))
    PY_list.append(int(input('PY 점수를 입력하세요.')))
    total_list.append(DB_list[n] + PY_list[n])
    ave_list.append(total_list[n]/2)
    print(f'이름:{name_list[n]} 학번:{id_list[n]} 성적합계:{total_list[n]} 평균:{ave_list[n]}')