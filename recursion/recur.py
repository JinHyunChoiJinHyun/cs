# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    
    if n > 0:
        recur(n - 1) 
        print(n) 
        recur(n - 2)
        # (4) 5 (3) => 1, 2, 3, 1, 4, 1, 2, 5, 1, 2, 3, 1
x = int(input("정수를 입력하세요.: "))

recur(x)