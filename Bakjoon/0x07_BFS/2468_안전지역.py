from collections import deque
N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
ans = []
maxnum = 0
for _ in range(N):
    a = list(map(int, input().split()))
    board.append(a)
    for i in a:
        if i > maxnum:
            maxnum = i
q = deque()
for k in range(maxnum):
    num = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > k and visited[i][j] == 0:
                q.append((i,j))
                num += 1
                visited[i][j] = 1
            while q:
                x , y = q.popleft()
                for dir in range(4):
                    nx = x+dx[dir]
                    ny = y+dy[dir]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]>k:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx,ny))
    ans.append(num)
print(max(ans))