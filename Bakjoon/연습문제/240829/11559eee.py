import sys
input = sys.stdin.readline
from collections import deque
graph = []
dx = [-1,1,0,0] ; dy = [0,0,-1,1]
for _ in range(12):
    graph.append(list(map(str,input())))
def boom(a,b):
    global don
    vis= [[0]*(6) for _ in range(12)]
    q = deque()
    q.append((a,b))
    same = set()
    while q:
        x,y = q.popleft()
        vis[x][y] = 1
        val = graph[x][y]
        same.add((x,y))
        for dir in range(4):
            nx,ny = x + dx[dir], y + dy[dir]
            if 0<=nx<12 and 0<=ny < 6 and vis[nx][ny] == 0:
                if val == graph[nx][ny] :
                    same.add((nx,ny))
                    q.append((nx,ny))

    if len(same) >= 4 :
        don = 1
        print("same:", *same)
        for i, j in same:
            graph[i][j] = '.'
def down():
    while True:
        flag = 0
        for i in range(11,0,-1): # 11 ~ 1 까지만
            for j in range(6):
                if graph[i][j] == '.' and graph[i-1][j] != '.':
                    graph[i][j] ,graph[i-1][j] = graph[i-1][j] , graph[i][j]
                    flag = 1
        if flag == 0:
            break
ans = 0
while True:
    don = 0

    vis = [[0] * (6) for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if vis[i][j] == 0 and graph[i][j] != '.':
                boom(i,j)
                vis[i][j]= 1
    if don == 0:
        break
    ans += 1
    down()
   # print("=======")
   # print("don:",don)
    for i in graph:
        print(*i)
print(ans)