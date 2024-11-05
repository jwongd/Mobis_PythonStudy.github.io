from collections import defaultdict, deque

n = int(input())
arr1 = [i for i in range(1, n + 1)]
arr2 = defaultdict(list)
ans2 = []
vis = [0] * (n + 1)
same = 0

for idx in range(1, n + 1):
    x = int(input())
    if idx == x:
        vis[x] = 1
        same += 1
        ans2.append(x)
        continue
    arr2[idx].append(x)


def bfs(st):
    q = deque([st])
    trace = []
    visited_local = set()

    while q:
        x = q.popleft()
        if x in visited_local:
            # Cycle detected
            cycle_start_index = trace.index(x)
            cycle_elements = trace[cycle_start_index:]
            for elem in cycle_elements:
                vis[elem] = 1
            ans.extend(cycle_elements)
            return
        visited_local.add(x)
        trace.append(x)
        for neighbor in arr2[x]:
            if not vis[neighbor]:
                q.append(neighbor)

    # 마크 탐색 완료 후 모든 노드 방문 표시
    for elem in trace:
        vis[elem] = 1


ans = []
for i in range(1, n + 1):
    if vis[i] == 0:
        bfs(i)

ans = list(set(ans))  # 중복 제거
ans_len = len(ans) + same  # 순환되는 모든 노드의 길이 + 자기 자신으로 돌아오는 노드의 수

print(ans_len)
fin = sorted(ans2 + ans)
for node in fin:
    print(node)
