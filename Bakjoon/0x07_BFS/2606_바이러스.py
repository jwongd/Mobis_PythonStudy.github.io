from collections import deque
N = int(input())
M = int(input())
q = deque()
com = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    x, y = map(int,input().split())
    com[x][y] = 1
    com[y][x] = 1
q.append(1)
visit[1] = 1
cnt = 0
while q:
    x = q.popleft()
    for i in range(1,N+1):
        if com[x][i] == 1 and visit[i] == 0: #연결여부 확인
            visit[i] = 1
            q.append(i)
            cnt += 1
print(cnt)
