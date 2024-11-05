from collections import defaultdict

def dfs(node, vis, st):
    # 방문하지 않은 노드를 계속 따라갑니다
    while node not in vis:
        vis.add(node)  # 노드를 방문 처리합니다
        st.append(node)
        node = graph[node][0]  # 다음 노드로 이동합니다

    # 사이클을 찾았다면 해당 사이클을 반환합니다
    if node in st:
        cycle_start = st.index(node)
        return st[cycle_start:]
    return None  # 사이클이 없으면 None을 반환합니다
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(n):
        graph[i + 1].append(arr[i])
    vis = set()
    ans = 0
    # 모든 노드에 대해 DFS를 수행합니다
    for i in range(1, n + 1):
        if i not in vis:  # 방문하지 않은 노드에 대해서만 DFS를 수행합니다
            result = dfs(i, vis, [])
            if result:
                # 사이클을 찾으면 그 길이를 ans에 더합니다
                ans += len(result)
    # 사이클에 포함되지 않은 학생 수를 출력합니다
    print(n - ans)