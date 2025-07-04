# 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any

class FixedQueue:
    
    class Empty(Exception):
        """비어있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
        
    def __len__(self) -> bool:
        """큐에 있는 모든 데이터 개수 반환"""
        return self.no
    
    def is_empty(self) -> bool:
        """큐가 비어있는지 판단"""
        return self.no <= 0
    
    def is_full(self) -> bool:
        """큐가 가득 차있는지 판단"""
        return self.no >= self.capacity
    
    def enque(self, x:Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity: # rear가 크기보다 커질 시 초기화
            self.rear = 0
            
    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        
        return x
    
    def peek(self) -> Any:
        """큐에서 데이터를 피크(맨 앞 데이터를 들여다 봄)"""
        if self.is_empty():
            raise FixedQueue.Empty
        
        return self.que[self.front]
    
    def find(self, value:Any) -> Any:
        """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity # front의 위치가 바뀌기 때문에 i에서 front를 더해준 후 계산 & front가 0이 되어야 함 => 선형 계산은 배열의 첫번째부터 돌아야하고 그렇지 않으면 삭제된 값을 보게 될 수도 있음 (no의 수가 바뀌기 때문)
            
            if self.que[idx] == value:
                return idx
            
    def count(self, value:Any) -> int:
        """큐에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value:Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.no = self.front = self.rear = 0
        
    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 맨 끝 순으로 출력"""
        if self.is_empty():
            print("큐가 비었습니다")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end="")
            print()
    