print("1부터 n까지 정수의 합을 구합니다.")

while True:
    n = int(input("n값을 입력하세요."))
    
    if n > 0:
        break
    
total = 0

for i in range(1, n+1):
    total += i
    
print(f"1부터 {n}까지 정수의 합은 {total}입니다.")
    