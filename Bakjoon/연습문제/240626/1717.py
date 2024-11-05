import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
def find(a):
    if parent[a] != a:
        parent[a]= find(parent[a])
    return parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a>=b:
        parent[a] = b
    elif a<b:
        parent[b] = a
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        union(b,c)
    elif a == 1:
        if find(b) != find(c):
            print("NO")
        else:
            print("YES")