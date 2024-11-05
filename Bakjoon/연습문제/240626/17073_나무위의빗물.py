from collections import defaultdict
graph = defaultdict(list)
n,m = map(int,input().split()) #m만큼 고여있음
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b) # a가 b의 부모
vis = [0] * (n+1)
def dfs(node):
    x = len(graph[node])
    for i in graph[node]:
        vis[i] = m/x
        dfs(i)
dfs(1)