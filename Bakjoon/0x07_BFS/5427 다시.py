from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
    flag = 0
    x, y = map(int,input().split())
    graph = []
    q_person = deque()
    q_fire  = deque()
    vis = [[0]*x for _ in range(y)]
    vis_f = [[0] * x for _ in range(y)]
    for _ in range(y):
        graph.append(list(input()))
    col = len(graph[0]) #열
    row = len(graph) #행
    for i in range(row):
        for j in range(col):
            if graph[i][j] == '@':
                q_person.append((i,j))
                vis[i][j] = 1
            if graph[i][j] == '*':
                q_fire.append((i,j))
                vis_f[i][j] = 1

    while q_fire:
        x_fire, y_fire = q_fire.popleft()
        for dir in range(4):
            nx_f = x_fire + dx[dir]
            ny_f = y_fire + dy[dir]
            if 0 <= nx_f < row and 0 <= ny_f < col and graph[nx_f][ny_f] != '#':
                q_fire.append((nx_f, ny_f))
                vis_f[nx_f][ny_f] = vis_f[x_fire][y_fire] + 1
    while q_person:
        x , y = q_person.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y+  dy[dir]
            if nx < 0 or nx >= row or ny<0 or ny>=col:
                print(vis[x][y])
                flag = 1
                break
            if graph[nx][ny] == '#' or graph[nx][ny] == '*' or vis[nx][ny]!=0:
                continue
            if vis_f[nx][ny] != 0 and vis_f <= vis[x][y] + 1:
                continue
            q_person.append((nx,ny))
            vis[nx][ny] = vis[x][y] + 1
    if flag == 0:
        print("IMPOSSIBLE")
