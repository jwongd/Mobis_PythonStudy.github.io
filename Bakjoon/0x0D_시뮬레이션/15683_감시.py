from collections import deque
n,m = map(int,input().split())
dr_1 = [[-1,0],[1,0],[0,1],[0,-1]] #dr_1[0] = [-1,0]
dr_2 = [[[-1,0],[1,0]],[[0,1],[0,-1]]] #dr_2[0] = [[-1,0],[1,0]]
dr_3 = [[[-1,0],[0,1]],[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]]]
dr_4 = [[[1,0],[0,1],[0,-1]],[[-1,0],[0,1],[0,-1]],[[-1,0],[1,0],[0,-1]],[[-1,0],[1,0],[0,1]]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
cnt = 0
def bfs5(i,j):
    global graph
    q = deque()
    for dir in range(4): # 5번 CCTV : 0~3 , 1번 CCTV : 0
        q.append([i,j,dir])
    while q:
        x,y,direction = q.popleft()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or nx>= n or ny<0 or ny>=m or graph[nx][ny] == 6:
            continue
        if graph[nx][ny] in range(1,6):
            q.append([nx,ny,direction])
            continue
        graph[nx][ny] = -1
        q.append([nx, ny, direction])


for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] in range(1,5): #1~4
            cnt+= 1
for i in range(n):
    for j in range(m):
        if graph[i][j] in range(1,6): # 1~5
            x = graph[i][j]
            if x == 5:
                bfs5(i,j)
            else:
                bfs(i,j)
print(*graph)





