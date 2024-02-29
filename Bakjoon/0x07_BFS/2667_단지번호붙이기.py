from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
areas = []
board = []
n = int(input())
visited = [[0]*(n+1) for _ in range(n+1)]
num = 0
for i in range(n):
    board.append(list(map(int,input())))
for i in range(n):
    for j in range(n):
        if board[i][j] == 0 or visited[i][j]==1:
            continue
        num += 1
        q.append((i,j))
        visited[i][j] = 1
        area = 0
        while q:
            area += 1
            x,y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if visited[nx][ny] == 1:
                    continue
                if 0<= nx < n and 0<= ny< n and board[nx][ny]!=0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        areas.append(area)
print(num)
areas.sort()
for i in areas:
    print(i)