# seq_search() 함수를 사용하여 실수 검색하기

from ssearch_while import seq_search

print("실수를 검색합니다.")
print("주의: 'End'를 입력하면 종료합니다.")

number = 0
x = []

while True:
    s = input(f"x[{number}]: ")
    # End 입력 시 값 입력 종료
    if s == "End":
        break
    
    x.append(float(s))
    number += 1
    
ky = float(input("검색할 값을 입력하세요."))

idx = seq_search(x, ky)

if idx == -1:
    print("검색 결과가 없습니다.")
    
else:
    print(f"x[{idx}]입니다")