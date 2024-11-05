import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    depth = [0] *(n+1) ; root = 0
    child = [[] for _ in range(n + 1)]
    parent = [-1] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        child[a].append(b)
        parent[b] = a
    x,y = map(int,input().split())
    for i in range(1,n+1):
        if parent[i] == -1:
            root = i
    #print("root:",root)
    def bfs(r):
        vis = [0] * (n + 1)
        vis[r] = 1
        q = deque()
        q.append(r)
        while q:
            x = q.popleft()
            for i in child[x]:
                if vis[i] == 0:
                    vis[i] = 1
                    q.append(i)
                    depth[i] = depth[x] + 1
    def make_samedepth(a,b):
        a1 = depth[a]
        b1 = depth[b]
       # print("a1:",a1,"b1:",b1)
        if a1 <= b1: #depth 큰 애를 끄집어 올려야함
            for _ in range(b1-a1):
                b = parent[b]
        else:
            for _ in range(a1-b1):
                a = parent[a]
       # print("a;",a,"b;",b)
        if a== b: return a
        while True:
            a = parent[a]
            b = parent[b]
            if a== b: break
        return a

    bfs(root) #depth update
    #print(*parent)
    ans = make_samedepth(x,y)
    print(ans)