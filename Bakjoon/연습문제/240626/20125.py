from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
print(*graph)
vis = [[0]*(n)for _ in range(n)]
q = deque() ; head_x,head_y = 0,0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if graph[i][j] == '*':
        #    q.append((i,j))
            head_x,head_y = i,j
            vis[i][j] = 1
            break
print("head:",head_x,head_y)
heart_x,heart_y = head_x+1,head_y # 0 - index 주의
q.append((heart_x,heart_y,0,0,0))
# 순서 : 아래, 오른, 왼 순서
dx = [1,0,0]
dy = [0,1,-1]
hurri , left_arm, right_arm = 0,0,0
while q:
    x,y,h,l,r = q.popleft()
    for dir in range(3):
        nx, ny= x + dx[dir] , y +dy[dir]
        if 0<=nx<n and 0<=ny<n :
            if vis[nx][ny] == 0 :
                if dir == 0:
                    h+=1
                elif dir == 1:
                    r+=1
                elif dir == 2:
                    l+=1
                q.append((nx, ny,h,l,r))
                vis[nx][ny] = 1
            else:
                if dir == 1:
                    last_hurri = x,y
    if len(q) == 0:
        hurri = h ; right_arm = r; left_arm = l
print("hurri:",hurri,"right_arm:",right_arm,"left:",left_arm)



