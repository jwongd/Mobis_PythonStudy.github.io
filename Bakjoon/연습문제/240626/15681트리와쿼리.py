from collections import defaultdict
graph = defaultdict(list)
n,r,q = map(int,input().split())
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
arr = [0] * (n+1)
def dfs(root):
    for i in graph[root]:
        dfs(i)
        arr[root] += 1



dfs(r)
for _ in range(q):
    a = int(input())
    print(arr[a])
