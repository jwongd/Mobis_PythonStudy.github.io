from collections import deque
q = deque()
N,M,V = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
list = []
list2 = []
visit = [0]*(N+1)
visit2 = [0]*(N+1)
for _ in range(M):
    a , b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    list2.append(v)
    visit2[v] = 1
    for i in range(1,N+1):
        if visit2[i]==0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q.append(v)
    visit[v] = 1
    while q:
        a = q.popleft()
        list.append(a)
        for i in range(1,N+1):
            if visit[i]==0 and graph[a][i] == 1:
                q.append(i)
                visit[i] = 1

bfs(V)
dfs(V)

print(*list2)
print(*list)