from collections import deque
T= int(input())
for _ in range(T):
    board = [[0]*51 for _ in range(51)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    n,m,k = map(int,input().split())
    vis = [[False] * m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        board[a][b] = 1
    num = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 or vis[i][j] == 1:
                continue
            num += 1
            q.append((i,j))
            vis[i][j] = True
            while q:
                x,y = q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if vis[nx][ny] == 1 or board[nx][ny] != 1:
                        continue
                    vis[nx][ny] = 1
                    q.append((nx, ny))
    print(num)



