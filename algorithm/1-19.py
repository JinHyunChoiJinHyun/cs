# 1~12까지 8을 건너뛰고 출력하기 -> 숫자가 커질수록 연산 횟수가 많아져 비효율적

for i in range(1, 13):
    if i == 8:
        continue

    print(i, end=" ")
