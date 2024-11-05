import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict,deque
n,r = map(int,input().split()) # root : r
tree = defaultdict(list)
child = defaultdict(list)
giga = 0
for _ in range(n-1):
    a,b,d = map(int,input().split())
    tree[a].append((b,d))
    tree[b].append((a,d))
def bfs(r):
    vis = [0] * (n+1)
    q = deque()
    q.append(r)
    vis[r] = 1
    while q:
        x = q.popleft()
        for node,dist in tree[x]:
            if vis[node] == 0:
                vis[node] = 1
                child[x].append((node,dist))
                q.append(node)
def find(r):
    q = deque()
    q.append(r) ; vis = [0] * (n+1)
    if len(child[r]) > 1 : return r
    while q:
        x = q.popleft()
        for node,_ in child[x]:
            if vis[node] == 0:
                if len(child[node]) > 1:
                    return node
                vis[node] = 1
                q.append(node)
    return x
def core_length(r):
    ans = 0
    q = deque()
    q.append(r)
    while q:
        x = q.popleft()
        if x == giga:
            return ans
        for i,d in child[x]:
            ans += d
            q.append(i)
def dfs_long(r):
    mx = 0
    if len(child[r]) == 0:
        return 0
    for i , d in child[r]:
        child_distance = dfs_long(i)
        mx = max(mx,child_distance + d)
    return mx


bfs(r)
l = 0 # giga --> leaf 최대값
giga = find(r)
core_l = core_length(r)
l = dfs_long(giga)
# print(child)
# print("giga:",giga)
# print(core_l)
# print(l)
print(core_l,l, end=' ')
