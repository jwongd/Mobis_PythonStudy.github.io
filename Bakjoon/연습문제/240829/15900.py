import sys
input = sys.stdin.readline
from collections import defaultdict , deque
n = int(input())
tree = defaultdict(list)
# depth의 값을 모두 구하면됨
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
child = defaultdict(list)
q = deque()
q.append(1)
vis = [0] *(n+1)
vis[1] = 1
while q:
    x = q.popleft()
    for i in tree[x]:
        if vis[i] == 0:
            child[x].append(i)
            q.append(i)
            vis[i] = vis[x] + 1
#print(child)
#print(*vis)
leaf = []
for i in range(2,n+1):
    if child[i]: continue
    leaf.append(i)
ans = 0
for i in leaf:
    ans += (vis[i] - vis[1])
#print(ans)
if ans % 2 == 0:
    print("No")
else:
    print("Yes")