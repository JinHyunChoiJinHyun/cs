# 1부터 12까지 8을 건너뛰고 출력하기 -> list를 꺼내서 반복하므로 여전히 연산 비용 발생

for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=" ")