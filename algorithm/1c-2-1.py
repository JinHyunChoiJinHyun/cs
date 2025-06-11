# 세 정수를 입력받아 중앙값 구하기 (비효율적인 코드 -> a와 b의 비교가 이미 끝났는데 다시 비교할 필요 없음)

def med3(a,b,c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    else:
        return c
    
    