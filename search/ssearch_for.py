# for문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    for i in range(len(a)):
                
        if a[i] == key:
            return i
    return -1

if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요."))
    
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
        
    ky = int(input("검색할 값을 입력하세요."))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print("검색 결과가 없습니다.")
    else:
        print(f"x[{idx}]에 있습니다")
        
        
