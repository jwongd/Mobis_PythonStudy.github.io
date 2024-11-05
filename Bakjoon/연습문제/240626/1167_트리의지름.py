from collections import defaultdict , deque
v = int(input()); graph = defaultdict(list)
for _ in range(v):
    arr = list(map(int,input().split()))
    num = arr[0]
    a = (len(arr) - 2)//2
    arr = arr[1:]
    for i in range(a):
        x,y = arr[2*i] , arr[2*i+1]
        graph[num].append((x,y))
# print(graph)
def bfs(st):
    vis = [-1] * (v+1)
    q = deque()
    q.append(st)
    vis[st] = 0
    while q:
        x = q.popleft()
        for nod,dist in graph[x]:
            #print("nod:",nod,"dist:",dist)
            if vis[nod] == -1:
                vis[nod] = dist + vis[x]
                q.append(nod)
    return vis
vis2 = (bfs(1))
mx = -1
for i in range(len(vis2)):
    if vis2[i] > mx:
        mx = vis2[i]
        ans = i
vis3 = bfs(ans)
print(max(vis3))