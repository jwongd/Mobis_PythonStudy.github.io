from collections import deque
N, K = map(int,input().split())
arr = [0]*200001
visited = [False]*200001
q= deque()
q.append(N)
visited[N] = 1
while q:
    x = q.popleft()
    list = [x+1,x-1,2*x]
    for i in list:
        if 0<= i < len(arr) and visited[i] == 0:
            visited[i] = 1
            q.append(i)
            arr[i] = arr[x]+1
print(arr[K])

