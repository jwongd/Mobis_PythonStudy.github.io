from collections import deque
n,w,L = map(int,input().split())
truck = list(map(int,input().split()))
truck.sort()
q = deque(truck)
bridge = []
ans = 0

while q:
    while len(bridge)<=w and sum(bridge)+q[0] <= L:
        x = q.popleft()
        bridge.append(x)
    ans = w + 1 - len(bridge)


