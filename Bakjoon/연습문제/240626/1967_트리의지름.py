from collections import defaultdict,deque
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # graph[부모] = cost, 자식
    graph[b].append((a, c))  # graph[부모] = cost, 자식
#print(graph)
def bfs(st):
    vis = [-1]*(n+1)
    q = deque()
    q.append(st)
    vis[st] = 0
    while q:
        x = q.popleft()
        for nod,dist in graph[x]:
            if vis[nod] == -1:
                vis[nod] = dist + vis[x]
                q.append(nod)
    return vis
a = (bfs(1))
mx = -1;v = 0
for i in range(len(a)):
    if mx < a[i] :
        v = i
        mx = a[i]
# print(a)
# print(v,mx)
b = (bfs(v))
# print(*b)
print(max(b))
