from collections import deque
n , k = map(int,input().split())
q = deque()
q.append((n,0))
cnt = 0
mx = max(n,k)
vis = [0]*(200001)
while q:
    x , c= q.popleft()
    if x == k:
        cnt = c
        break
    if 0<= 2*x <= 100000 and vis[2*x] == 0:
        vis[2*x] = 1
        q.appendleft((2*x,c))
    for i in [x-1,x+1]:
        if vis[i] == 0 and 0<=i <=100000:
            vis[i] = 1
            q.append((i,c+1))

print(cnt)