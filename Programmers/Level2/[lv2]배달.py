import heapq
def sol(N,road,K):
    ans = 0
    graph = [[] for _ in range(N+1)]
    dist = [float("inf" for _ in range(N+1))]
    dist[1] = 0
    for st,en,cost in road:
        graph[st].append([en,cost])
        graph[en].append([st,cost])
    heap = []
    heapq.heappush(heap,(0,1))
    while heap:
        cost, cur = heapq.heappop(heap)
        if dist[cur] < cost:
            continue
        for nxt, c in graph[cur]:
            tot = cost + c
            if tot < dist[nxt]:
                dist[nxt] = tot
                heapq.heappush(heap,(tot,nxt))
    for i in dist[1:]:
        if i <= K:
            ans+=1
    return ans