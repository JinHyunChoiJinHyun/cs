# 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    
    a = copy.deepcopy(seq) # seq 복사
    a.append(key) # 마지막에 key 추가 => 배열에 값이 없더라도 while문을 중단하기 위해서 // 보초 값이 없으면 무한 루프에 빠짐
    
    i = 0
    while True:
        if a[i] == key:
            break
        
        i += 1
        
    return -1 if i == len(seq) else i # i가 seq의 len과 같다면 -1 반환 아니면 i 반환

if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요."))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
        
    ky = int(input("검색할 값을 입력하세요"))
    
    idx = seq_search(x, ky)
        
    if idx == -1:
        print("검색 값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"x[{idx}]에 있습니다.")
    