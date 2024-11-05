import sys
from heapq import heappop,heappush
input = sys.stdin.readline
n = int(input())
max_h = []
min_h = []
if n == 1:
    a = int(input())
    print(a)
    exit(0)
a = int(input())
print(a)
b = int(input())
x = min(a,b)
if a>=b:
    heappush(max_h,-b)
    heappush(min_h,a)
else:
    heappush(max_h, -a)
    heappush(min_h, b)
print(x)
for _ in range(n-2): #첫케이스는 홀수
    a = int(input())
    if a <= -max_h[0]: # ????
        heappush(max_h,(-1)*a)
    else:
        heappush(min_h,a)
    #문제의 조건에서 짝수에서는 min값을 택한다고 했으므로
    if len(max_h) > len(min_h)+1: # 최대힙의 크기가 최소힙 크기 + 1보다 크면
        heappush(min_h,-heappop(max_h))
    elif len(min_h) > len(max_h): # 최소힙의 크기가 최대힙의 크기보다 크면
        heappush(max_h,-heappop(min_h))
    if len(max_h) >= len(min_h):
        print(-max_h[0])
    else:
        print(min_h[0])

if a >= min_h[0]:
    heappush(max_h, (-1) * a)
else:
    heappush(min_h, a)