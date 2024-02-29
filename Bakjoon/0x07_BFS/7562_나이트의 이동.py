import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]
for _ in range(T):
    I = int(input())
    board = [[0]*I for _ in range(I)]
    q = deque()
    vis = [[False]*I for _ in range(I)]
    a, b = map(int,input().split())
    c, d = map(int,input().split())
    q.append((a,b))
    vis[a][b] = True
    board[a][b] = 0
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            print(board[c][d])
            break
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<I and 0<=ny<I and vis[nx][ny] == 0 :
                vis[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))



