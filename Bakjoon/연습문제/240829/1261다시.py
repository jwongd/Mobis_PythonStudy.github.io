import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]


def bfs():
    q = deque([(0, 0, 0)])  # x, y, walls_broken
    vis = set([(0, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, walls = q.popleft()

        if x == n - 1 and y == m - 1:
            return walls

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis:
                vis.add((nx, ny))
                if graph[nx][ny] == 0:
                    q.appendleft((nx, ny, walls))
                else:
                    q.append((nx, ny, walls + 1))

    return -1  # If no path is found


print(bfs())