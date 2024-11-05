import sys
input = sys.stdin.readline
def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(graph[nx][ny]) - ord('A')]:
            visited[ord(graph[nx][ny]) - ord('A')] = True
            dfs(nx, ny, count + 1)
            visited[ord(graph[nx][ny]) - ord('A')] = False
R, C = map(int, input().split())
graph = [input().strip() for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
visited = [False] * 26  # A부터 Z까지 26개의 알파벳
visited[ord(graph[0][0]) - ord('A')] = True
dfs(0, 0, 1)
print(answer)