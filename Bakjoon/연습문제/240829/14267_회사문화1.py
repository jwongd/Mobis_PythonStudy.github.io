from collections import defaultdict
n , m = map(int,input().split())
arr = list(map(int,input().split()))
parent = [-1] * (n+1) # 직속상사
ans = [0]*(n+1)
child = defaultdict(list)

def dfs(r,w):
    for i in child[r]:
        dfs(i,w+ans[i])

for idx,val in enumerate(arr,1):
    parent[idx] = val
for _ in range(m):
    ss,w = map(int,input().split())
    ans[ss] += w
    dfs(ss,w)


