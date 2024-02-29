from collections import deque
n,k = map(int,input().split())
q = deque()
q.append(n)
vis = [-1] * 100001
vis[n] = 0
while q:
    x = q.popleft()
    if x == k:
        print(vis[x])
        break
    for i in [x-1,x+1,x*2]:
        if 0<=i <= 100000 and vis[i] == -1:
            if i == x*2:
                vis[i] = vis[x]
                q.appendleft(i)
            else:
                vis[i] = vis[x] + 1
                q.append(i)
