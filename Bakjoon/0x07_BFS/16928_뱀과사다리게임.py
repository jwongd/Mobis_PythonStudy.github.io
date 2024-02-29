from  collections import deque
n,m = map(int,input().split())
graph1 = {}
snake = {}
for _ in range(n):
    x,y = map(int,input().split())
    graph1[x] = y
for _ in range(m):
    x,y = map(int,input().split())
    snake[x] = y

vis = [-1]*102

q = deque([1])
vis[1] = 0
while q:
    x = q.popleft()
    for dir in range(1,7):
        nx = x+dir
        if 0<nx<=100:
            if nx in graph1:
                nx = graph1[nx]
            if nx in snake:
                nx = snake[nx]
            if vis[nx] == -1:
                vis[nx] = vis[x]+1
                q.append(nx)
print(vis[100])