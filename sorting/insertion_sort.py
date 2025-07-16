# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp: # 선택한 값이 왼쪽의 값보다 작을 시 덮어쓰기
            a[j] = a[j-1] 
            j -= 1
        
        a[j] = tmp # 덮어쓴 값을 앞으로 이동

if __name__ == "__main__":
    print("단순 삽입 정렬을 수행합니다")
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
    
    insertion_sort(x)
    
    print("오름차순으로 정렬했습니다")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")