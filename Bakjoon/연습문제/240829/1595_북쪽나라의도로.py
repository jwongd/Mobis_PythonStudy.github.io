from collections import deque, defaultdict

# 변수 초기화
flag = 0
start = 1  # start 변수를 기본값 1로 초기화
graph = defaultdict(list)
distance = [-1] * 10001

def dfs(node, dist):
    global distance
    distance[node] = dist
    for nxt_node, nxt_dist in graph[node]:
        if distance[nxt_node] == -1:
            dfs(nxt_node, dist + nxt_dist)

# 입력 받기
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

# 입력이 비어있는 경우 처리
if not graph:
    print(0)
else:
    # 첫 번째 DFS
    dfs(start, 0)

    # 가장 먼 노드 찾기
    #end = start  # end의 초기값을 start로 설정
    max_dist = -1
    end = distance.index(max(distance))

    # 두 번째 DFS
    distance = [-1] * 10001
    dfs(end, 0)
    print(max(distance))