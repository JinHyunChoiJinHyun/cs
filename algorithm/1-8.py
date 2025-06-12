# 1부터 n까지 정수의 합 구하기 (for 문)

n = int(input("정수를 입력하세요."))
sum = 0

for i in range(1, n+1):
    sum += i
    print(f"i 값은 {i} 입니다.")
    
print(f"1부터 {n}까지의 총합은 {sum} 입니다.")