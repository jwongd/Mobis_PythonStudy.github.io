from collections import defaultdict, deque
n , m = map(int,input().split())
graph = defaultdict(list)
for _ in range(n-1):
    a,b,dist =  map(int,input().split())
    graph[a].append((dist,b))
    graph[b].append((dist,a))
def bfs(a,b): # a ~ b : 거리
    vis = [0] * (n + 1)
    q = deque()
    q.append((0,a))
    vis[a] = 1
    while q:
        dist, x = q.popleft()
        if x == b:
            return dist
        for cost, node in graph[x]:
            if vis[node] == 0 :
                q.append((dist+cost,node))
                vis[node] = 1
for _ in range(m):
    x,y =  map(int,input().split())
    print(bfs(x,y))
