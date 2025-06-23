# while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

# 함수 정의 => 매개변수 a는 sequence 타입, 매개변수 key는 아무 타입이나 가능 -> 정수 값을 반환
def seq_search(a: Sequence, key:Any) -> int: 
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    
    i = 0
    
    while True:
        # a에 key와 일치하는 값이 없을 시
        if i == len(a):
            return -1 # 검색 실패
        # a 내부에서 key와 일치하는 값을 찾을 시
        if a[i] == key: 
            return i # 검색에 성공하여 현재 인덱스 값 반환
        
        # index의 값이 key와 일치하지 않을 시
        i += 1
        
if __name__ == "__main__":
    # 배열의 크기 설정
    num = int(input("원소 수를 입력하세요."))
    
    x = [None] * num
    
    # 배열에 값 입력
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
        
    # key 값 입력        
    ky = int(input("검색할 값을 입력하세요."))
    
    # 함수에 값 입력
    idx = seq_search(x, ky)
    
    # 결과 표출
    if idx == -1:
        print("검색 값이 없습니다.")
    else:
        print(f"검색 값은 x[{idx}]에 있습니다.")
            
    