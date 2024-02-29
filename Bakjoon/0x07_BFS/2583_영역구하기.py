from collections import deque
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
num = 0
areas = []
m, n, k = map(int,input().split())
board = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1, x2):
            board[i][j] = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            continue
        board[i][j] = 1
        area = 1
        num += 1
        q.append((i,j))
        while q:
            x , y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0<= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                    area+= 1
                    board[nx][ny] = 1
                    q.append((nx,ny))
        areas.append(area)
print(len(areas))
areas.sort()
for i in areas:
    print(i,end=' ')
    


