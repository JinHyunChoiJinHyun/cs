# 10 ~ 99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input("난수의 개수를 입력하세요."))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=" ")
    if r == 13:
        print("\n프로그램을 중단합니다.")
        break
    
else: # for문에도 else 사용 가능 for문이 정상적으로 종료되었으나 조건에 맞는게 없을 때 실행 (break가 없을 때)
    print("\n 난수 생성을 종료합니다.")