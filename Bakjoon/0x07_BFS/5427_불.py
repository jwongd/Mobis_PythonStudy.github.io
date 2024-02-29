from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for _ in range(T):
    w,h = map(int,input().split())
    graph = []
    for i in range(h):
        graph.append(list(input()))
    sg = deque()
    fire = deque()
    ans = [-1]
    dis_s = [[-1]*(w) for _ in range(h)]
    dis_f = [[-1]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                sg.append((i,j))
                dis_s[i][j] = 0
            if graph[i][j] == "*":
                fire.append((i,j))
                dis_f[i][j] = 0

    while fire:
        x,y = fire.popleft()
        for dir in range(4):
            nx = x+ dx[dir]
            ny = y+ dy[dir]
            if 0 <= nx < h and 0 <= ny < w and dis_f[nx][ny] == -1:
                if graph[nx][ny] == "#" or graph[nx][ny] == "*":
                    continue
                dis_f[nx][ny] = dis_f[x][y] + 1
                fire.append((nx,ny))
    while sg:
        x,y = sg.popleft()
        for dir in range(4):
            nx = x+ dx[dir]
            ny = y+ dy[dir]
            if nx<0 or nx>=h or ny<0 or ny>=w :
                if dis_s[x][y] <= dis_f[x][y] or dis_f[x][y] == -1:
                    ans.append(dis_s[x][y]+1)
                    continue
                else:
                    continue
            else:
                if dis_s[nx][ny] == -1:
                    if graph[nx][ny] == "#":
                        continue
                    if dis_f[nx][ny] != -1 and dis_s[x][y]+1 >= dis_f[nx][ny]:
                        continue
                    dis_s[nx][ny] = dis_s[x][y] + 1
                    sg.append((nx,ny))

    if max(ans) == -1:
        print("IMPOSSIBLE")
    else:
        print(max(ans))


