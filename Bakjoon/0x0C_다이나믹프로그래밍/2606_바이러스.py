from collections import deque
q = deque()
N = int(input())
M = int(input())
list = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    list[a][b] = 1
    list[b][a] = 1
q.append(1)
visit[1] = 1
cnt = 0
while q:
    cnt += 1
    x = q.popleft()
    for i in range(1,N+1):
        if visit[i] == 0 and list[x][i] == 1:
            q.append(i)
            visit[i] = 1
print(cnt-1)
