# 구구단 곱셈표 출력하기

for i in range(1,10):
    for j in range(1,10):
        print(f"{i * j:3}", end="") # :3 => 각 요소가 3칸씩 차지
    print()