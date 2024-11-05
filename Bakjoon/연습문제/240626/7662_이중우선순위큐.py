import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    q = []
    for _ in range(n):
        com, val = map(str,input().split())
        val = int(val)
        if com == 'I':
            heapq.heappush(q,val)
        elif com == 'D':
            if val == 1 and q: # 최대값 삭제
                q.remove(heapq.nlargest(1,q)[-1])
            elif val == -1 and q: #최소값 삭제
                heapq.heappop(q)
    if q:
        x = heapq.nsmallest(1,q)[-1]
        y = heapq.nlargest(1,q)[-1]
        print(x,y,end = ' ')
    else:
        print("EMPTY")