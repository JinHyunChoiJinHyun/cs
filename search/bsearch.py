# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2 # 두 커서의 중앙값
        
        if a[pc] == key:
            return pc
        
        elif a[pc] < key:
            pl = pc + 1 # pc의 오른쪽
            
        else:
            pr = pc - 1 # pc의 왼쪽
        
        if pl > pr: # 검색 범위 앞 원소가 뒷 원소보다 커질 시 종료
            break
    return -1

if __name__ == "__main__":
    # 배열의 크기 설정
    num = int(input("원소 수를 입력하세요."))
    
    x = [None] * num
    
    print("배열 데이터를 오름차순으로 입력하세요.")
    
    x[0] = int(input("x[0]: "))
    
    # 배열에 값 입력
    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}]: "))
            if x[i] >= x[i-1]: # 바로 직전의 원소 값보다 큰 값 입력
                break # 조건이 맞지 않을 시 같은 반복문 반복
    
    # key 값 입력        
    ky = int(input("검색할 값을 입 력하세요."))
    
    # 함수에 값 입력
    idx = bin_search(x, ky)
    
    # 결과 표출
    if idx == -1:
        print("검색 값이 없습니다.")
    else:
        print(f"검색 값은 x[{idx}]에 있습니다.")
