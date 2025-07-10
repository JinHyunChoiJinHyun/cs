def n_queen(n):
    answer = 0
    col = [0] * n
    
    def is_safe(row):
        for i in range(row):
            if col[row] == col[i] or abs(col[row] - col[i]) == row - i: # row가 0일 시 루프가 실행되지 않음
                return False
            
        return True
        
        
    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        
        for i in range(n): # 모든 수에 대해서 is_safe 실행 safe가 아닐 시 진행하지 않고 넘어가기 (백트래킹)
            col[row] = i
            if is_safe(row):
                dfs(row+1)
                
    dfs(0)
    
    return answer

print(n_queen(8))