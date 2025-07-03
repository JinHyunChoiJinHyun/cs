# 체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum("Menu", ["추가", "삭제", "검색", "덤프", "종료"]) # 메뉴 선언 -> 생성자 함수 생성

"""class Menu(Enum):
    추가 = 1
    삭제 = 2
    검색 = 3
    덤프 = 4
    종료 = 5"""

def select_menu() -> Menu:
    """메뉴 선택"""
    
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep="    ", end="")
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
hash = ChainedHash(13)

while True:
    menu = select_menu()
    
    # 추가
    if menu == Menu.추가:
        key = int(input("추가할 키를 입력하세요.:"))
        val = input("추가할 값을 입력하세요.:")
        
        if not hash.add(key,val):
            print("추가를 실패했습니다!")
    
    # 삭제
    elif menu == Menu.삭제:
        key = int(input("삭제할 키를 입력하세요.:"))        
        if not hash.remove(key):
            print("삭제를 실패했습니다!")
            
    # 검색
    elif menu == Menu.검색:
        key = int(input("검색할 키를 입력하세요.:"))        
        t = hash.search(key)
        if t is not None:
            print(f"검색한 키를 갖는 값은 {t}입니다.")   
        else:
            print("검색할 데이터가 없습니다.")     
            
    #덤프
    
    elif menu == Menu.덤프:
        hash.dump()
        
    else:
        break