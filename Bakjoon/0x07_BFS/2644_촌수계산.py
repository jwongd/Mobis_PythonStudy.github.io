from collections import deque
q = deque()

n = int(input())
res = [0]*(n+1)
x,y = map(int,input().split())
visit = [[0]*(n+1)]
graph = [[0]*(n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q.append(x)
visit[x] = 1
while q:
    d = q.popleft()
    for i in graph[d]:
        if not visit[i]:
            q.append(i)
            res[i] = res[d] + 1
            visit[i] = True
if res[y] > 0 :
    print(res[y])
else:
    print(-1)
