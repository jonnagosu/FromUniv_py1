# 세 개의 정수를 입력 받습니다.
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
num3 = int(input("세 번째 정수를 입력하세요: "))

# 가장 큰 수를 찾습니다.
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# 결과를 출력합니다.
print(f"가장 큰 수는 {largest}입니다.")

# f는 (f-string)의 약자, 문자열 내부에 변수 값을 집어넣는 간편한 방법.
