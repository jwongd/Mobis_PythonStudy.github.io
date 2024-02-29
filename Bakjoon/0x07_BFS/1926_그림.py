from collections import deque

# 상하좌우 네 방향을 의미하는 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 해당 칸을 방문했는지 여부를 저장하는 리스트
vis = [[False] * m for _ in range(n)]

mx = 0  # 그림의 최댓값
num = 0  # 그림의 수

for i in range(n):
    for j in range(m):
        # (i, j)를 시작점으로 하고 싶은 상황
        if board[i][j] == 0 or vis[i][j]:
            continue  # 해당 칸이 색칠이 안된 부분(0)이거나 이미 (i, j)를 방문했을 경우 넘어감

        # (i,j)는 새로운 그림에 속해있는 시작점
        num += 1  # 그림의 수 1 증가
        Q = deque([(i, j)])
        vis[i][j] = True  # (i,j)로 BFS를 시작하기 위한 준비

        area = 0  # 그림의 넓이
        while Q:
            area += 1  # 큐에 들어있는 원소를 하나 뺄 때 마다 넓이를 1 증가시킴
            x,y = Q.popleft()
            for dir in range(4):  # 상하좌우 칸을 살펴볼 것이다.
                nx = x + dx[dir]
                ny = y + dy[dir]  # nx, ny에 dir에서 정한 방향의 인접한 칸의 좌표가 들어감
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue  # 범위 밖일 경우 넘어감
                if vis[nx][ny] or board[nx][ny] != 1:
                    continue  # 이미 방문한 칸이거나 파란 칸이 아닐 경우
                vis[nx][ny] = True  # (nx, ny)를 방문했다고 명시
                Q.append((nx, ny))

        # (i, j)를 시작점으로 하는 BFS가 종료됨
        mx = max(mx, area)  # area가 mx보다 클 경우 mx에 area를 대입. max는 내장 함수

print(num)
print(mx)
