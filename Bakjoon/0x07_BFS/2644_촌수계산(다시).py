from collections import deque
q = deque()
n = int(input())
a, b = map(int,input().split())
visit = [0]*(n+1)
dist = [-1]*(n+1)
graph =[[]*(n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
q.append(a)
visit[a] = 1
dist[a] = 0
while q:
    x1 = q.popleft()
    for i in graph[x1]:
        if visit[i] == 0 and dist[i] == -1:
            visit[i] = 1
            dist[i] = dist[x1]+1
            q.append(i)

print(dist[b])
