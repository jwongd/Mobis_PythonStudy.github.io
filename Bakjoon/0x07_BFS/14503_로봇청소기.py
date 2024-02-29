from collections import deque
n,m = map(int,input().split())
x_init,y_init,dir_init = map(int,input().split())
graph= []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
vis = [[0]*m for _ in range(n)]
q = deque()
q.append((x_init,y_init))
vis[x_init][y_init] = 1
ans = 1
while q:
    x,y = q.popleft()
    chk = 0
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if vis[nx][ny] == 0 and graph[nx][ny] == 0:
            chk = 1      # 주변 청소할 곳이 있으면 chk =1
    if chk == 0:
        nx = x - dx[dir_init]
        ny = y - dy[dir_init]
        if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny] ==1:
            break
        if vis[nx][ny] == 0:
            vis[nx][ny] = 1
            q.append((nx,ny))
            ans += 1
        else:
            continue
    elif chk == 1:
        for _ in range(4):
            dir_init = (dir_init+3)%4
            nx = x+dx[dir_init]
            ny = y+dy[dir_init]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if  graph[nx][ny]== 1 or vis[nx][ny]==1:
                continue
            vis[nx][ny] = 1
            q.append((nx,ny))
            ans+=1
            break
print(ans)
