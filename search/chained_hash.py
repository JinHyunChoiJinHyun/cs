# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""
    
    def __init__(self, key:Any, value:Any, next:Node) -> None:
        """초기화"""
        # ,를 붙이면 tuple로 생성됨
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드 참조

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self, capacity:int) -> None:
        """초기화"""
        self.capacity = capacity # 해시 테이블 크기 지정
        self.table = [None] * self.capacity # 해시 테이블 선언
    
    def hash_value(self, key:Any) -> int:
        """해시값을 구함"""
        
        if isinstance(key, int): # key가 int 타입이라면 조건문 실행
            return key % self.capacity

        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) # int 타입이 아닐 시 변환
    
    def search(self, key:Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드 확인
            
        return None # 검색 실패
    
    def add(self, key:Any, value:Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key) # 추가하는 key의 해시 값
        p = self.table[hash]
        
        while p is not None: # 값이 None이 아닐 시 -> 값이 이미 존재할 시
            if p.key == key: 
                return False # 추가 실패 (중복 방지)
            p = p.next # 뒤쪽 노드 확인
        
        # if문 통과 시 새로 추가
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드 추가
        return True # 추가 성공 (성공 / 실패 여부 확인)
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        
        while p is not None:
            if p.key == key: 
                if pp is None: # 삭제하려는 노드가 맨 앞에 위치할 시
                    self.table[hash] = p.next # 뒷 노드를 앞 노드로 대체
                else: # 삭제하려는 노드가 맨 앞에 존재하는 노드가 아닐 시
                    pp.next = p.next # 앞 노드의 next로를 삭제하려는 노드의 뒤에 있는 값을  대체
                return True
            
            # key와 값이 다를 시
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f" -> {p.key} ({p.value})", end="")
                p = p.next # 다음 노드가 없을 시 None
            print()                
        
        
            
        