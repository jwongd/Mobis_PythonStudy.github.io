import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n,w = map(int,input().split())
tree = [[] for _ in range(n+1)]
vis = [0] * (n+1)
child = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
# 루트는 항상 1번 정점, 리프노드의 개수를 구해서 w/리프노드
def dfs(r):
    for i in tree[r]:
        if vis[i] == 0:
            child[r].append(i)
            vis[i] = 1
            dfs(i)
vis[1] = 1
dfs(1)
#print(*child)
cnt = 0
for i in range(1,n+1):
    if len(child[i]) == 0:
        cnt+=1
print(w/cnt)