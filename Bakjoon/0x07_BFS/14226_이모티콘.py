from collections import deque
S = int(input())
vis = [0]*1000
q = deque([1])
while q:
    x = q.popleft()
    