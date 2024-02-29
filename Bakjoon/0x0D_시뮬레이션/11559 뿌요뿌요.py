from collections import deque
graph  = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
vis = [[0]*6 for _ in range(12)]
for _ in range(12):
    graph.append(list(input()))
q = deque()
ans = 0
while True:
    area = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j]  in ['R','G','B','P','Y']:
                vis[i][j] = 1
                q.append((i,j))
                break
    while q :
        q2 = deque()
        area += 1
        #print(area)
        x,y = q.popleft()
        q2.append((x,y))
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<12 and 0<=ny < 6:
                if vis[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                    q.append((nx,ny))
                    q2.append((nx,ny))
                    vis[nx][ny] = 1
    if area >= 4 :
        ans += 1
        while q2:
            a,b = q2.popleft()
            graph[a][b] = '.'
    else:
        print(ans)
        exit(0)
    flag = 0
    while True:
        for i in  range(11):
            for j in range(6):
                if graph[i][j] in ['R', 'G', 'B', 'P', 'Y'] and graph[i+1][j] == '.':
                    graph[i+1][j],graph[i][j] = graph[i][j] , graph[i+1][j]
                    flag = 1
        if flag == 0:
            break
# if check_num() == 1:






