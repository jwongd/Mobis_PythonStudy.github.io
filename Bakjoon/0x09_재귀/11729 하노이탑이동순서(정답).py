import sys
sys.setrecursionlimit(10**7)
n = int(input())
def hanoi(a,b,n): #출발,도착,남은횟수 (원판 n개를 a --> b로 옮기는 방법 출력)
    if n == 1:
        print(a,b)
        return
    hanoi(a,6-a-b,n-1)
    print(a,b)
    hanoi(6-a-b,b,n-1)
x = 2**n - 1
print(x)
hanoi(1,3,n)