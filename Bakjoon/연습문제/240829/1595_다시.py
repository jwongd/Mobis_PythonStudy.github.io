from collections import defaultdict, deque
import sys
input = sys.stdin.readline
# 입력 받기
graph = defaultdict(list) ; start = 0
flag = 0
while True:
    try:
        a, b, c = map(int, input().split())
        if flag == 0:
            start = a
            flag = 1
        graph[a].append([b, c])
        graph[b].append([a, c])
    except:
        break
def bfs(st):
    vis = [-1] * (10001)
    q = deque()
    ans = [0,0] # node,dist
    q.append((st,0)) #node,dist
    vis[st] = 0
    while q:
        node,dist = q.popleft()
        for nxt_node, nxt_dist in graph[node]:
            if vis[nxt_node] == -1:
                nxt_dist += dist
                vis[nxt_node] = nxt_dist
                q.append((nxt_node, nxt_dist))
                if nxt_dist > ans[1]:
                    ans[0] = nxt_node
                    ans[1] = nxt_dist

    return ans
# print(graph)
# print("start:",start)
a = bfs(start)
# print(*a)
res = bfs(a[0])[1]
print(res)