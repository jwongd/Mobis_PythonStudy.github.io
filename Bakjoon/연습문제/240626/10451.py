import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    vis = [0] * (n+1) ; ans = 0

    def bfs(a):
        q = deque()
        q.append(a)
        vis[a] = 1
        while q:
            x = q.popleft()
            i = arr[x]
            if vis[i] == 0:
                q.append(i)
                vis[i] = 1
    for i in range(1,n+1):
        if vis[i] == 0:
            bfs(i)
            ans += 1
    print(ans)

