n, m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*2001
ans = False
for i in range(m):
    a , b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
def dfs(idx, depth ):
    global  ans
    visited[idx] = True
    if depth == 4:
        ans = True
        return
    for i in range(1,n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i,depth+1)
            visited[i] = False
for i in range(1,n+1):
    dfs(i,0)
    visited = [False]*(n+1)
    if ans:
        break
if ans:
    print(1)
else:
    print(0)
