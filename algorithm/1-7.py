# 1부터 n까지 정수의 합 구하기 (while 문)

sum = 0
i = 1

n = int(input("정수를 입력해주세요."))

while i <= n:
    sum += i    
    i += 1
    print(f"i값은 {i} 입니다.")
print(f"1부터 {n}까지의 합은 {sum} 입니다.")
    