import sys
input = sys.stdin.readline
import heapq
n , m = map(int,input().split())
k = int(input())
INF = int(1e9)
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b)) #(c = 비용 , b = 도착노드)
def dijk (st):
    q = []
    distance[st] = 0
    heapq.heappush(q,(distance[st],st)) #비용, 정점번호
    while q:
        dist, nod = heapq.heappop(q)
        if distance[nod] != dist:
            continue
        for i in graph[nod]:
            cost = dist + i[0] # i[0] : 비용 , i[1] : 정점번호
            if cost < distance[i[1]]: # 다른 노드를 거쳐서 이동하는 게 더 짧다면?
                distance[i[1]] = cost # 업데이트
                heapq.heappush(q,(cost,i[1]))
dijk(k)
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
