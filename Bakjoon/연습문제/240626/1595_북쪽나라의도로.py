from collections import defaultdict
graph = defaultdict(list) ; n =0
while True:
    try:
        n += 1
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
    except:
        break
dist = [-1] * (10001)
def dfs(node,dis):
    for cost,nxt_node in graph[node]:
        nxt_dist = cost + dis
        if dist[nxt_node] == -1:
            dist[nxt_node] = nxt_dist
            dfs(nxt_node,nxt_dist)
    return

tmp = [0, 0]
dfs()
for i in range(1,10001):
    if dist[i] > tmp[1]:
        tmp[0] = i
        tmp[1] = dist[i]

