from collections import defaultdict, deque
n,k = map(int,input().split())
graph = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(st):
    q = deque()
    vis = [-1] * (n+1)
    q.append(st)