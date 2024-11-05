import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [-1] * n
children = defaultdict(list)
ans = [0] * n

arr = list(map(int, input().split()))
for i in range(1, n):
    parent[i] = arr[i] - 1
    if parent[i] != -2:  # -1에서 0-index로 변환되어 -2가 됨
        children[parent[i]].append(i)

def bfs(start, value):
    q = deque([(start, value)])
    while q:
        curr, val = q.popleft()
        ans[curr] += val
        for child in children[curr]:
            q.append((child, val))

for _ in range(m):
    i, w = map(int, input().split())
    bfs(i-1, w)  # 0-index로 변환

print(*ans)