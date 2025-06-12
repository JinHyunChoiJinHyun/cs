# *를 n개 출력하되 w개마다 줄바꿈하기 -> for 문을 반복할 때마다 if 문을 검사하여 비효율적

print("*를 출력합니다.")

n = int(input("몇 개를 출력할까요?"))
w = int(input("몇 개마다 줄바꿈 할까요?"))

for i in range(n):
    print("*", end="")
    
    if i % w == w - 1:
        print()
        
# if n % w:
#     print()