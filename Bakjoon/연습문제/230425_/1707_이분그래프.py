import sys
sys.setrecursionlimit(10**9)
k = int(input())
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x > y :
        parent[x] = y
    else:
        parent[y] = x
for _ in range(k):
    v,e =  map(int,input().split())
    parent = [i for i in range(1, 20001)]
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        union(parent,a,b)
    print(*parent)

