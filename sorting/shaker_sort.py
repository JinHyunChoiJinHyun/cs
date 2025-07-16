# 셰이커 정렬 알고리즘 구현하기

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    
    left = 0
    right = len(a) - 1    
    
    while left < right:
        new_right = left
        for j in range(right, left, -1): # 오른쪽 -> 왼쪽 큰수를 뒤로
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
        left = new_right        
        
        new_left = right
        
        for j in range(left, right): # 왼쪽 -> 오른쪽 작은 수를 앞으로
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        
        right = new_left
        
if __name__ == "__main__":
    print("버블 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))
    
    shaker_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")