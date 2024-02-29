import heapq
from collections import deque
N,L = map(int,input().split())
num = list(map(int,input().split()))
ans = []
for i in range(N):
    h = []
    # print("===============")
    if i < L:
        x = num[:i+1]
        # print("x:",x)
        heapq.heapify(x)
        y = x[0]
        # print("y:", y)
        ans.append(y)
    else:
        x = num[i-L+1:i+1]
        # print("x:", x)
        heapq.heapify(x)
        y = x[0]
        # print("y:", y)
        ans.append(y)
result = ' '.join(map(str,ans))
print(result)