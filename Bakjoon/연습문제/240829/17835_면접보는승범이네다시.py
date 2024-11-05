import heapq ,sys
input = sys.stdin.readline
from collections import defaultdict,deque
n,m,k = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    u,v,c = map(int,input().split())
    #graph[u].append((v,c)) #단방향이므로 삭제해야함
    graph[v].append((u,c))
arr = list(map(int,input().split())) # 면접장이 배치된 도시의 번호
q = [] ; INF = int(1e10)
distance = [INF] * (n+1)
for i in arr:
    heapq.heappush(q,(i,0)) #면접장 다 queue에 넣기 (node,dist)
    distance[i] = 0
def dijk():
    global distance
    while q:
        node,dist = heapq.heappop(q)
        if distance[node] != dist: continue
        for nxt_node, nxt_dist in graph[node]:
           # print("nd:",nxt_node,"nx_dst:",nxt_dist)
            if distance[nxt_node] >= dist + nxt_dist :
                distance[nxt_node] = dist + nxt_dist
                heapq.heappush(q,(nxt_node,distance[nxt_node]))
dijk()
max_start , max_cost = 0,0
#print(*distance)
for index, val in enumerate(distance):
    if val > max_cost and val != INF:
        max_start , max_cost = index,val
print(max_start)
print(max_cost)

