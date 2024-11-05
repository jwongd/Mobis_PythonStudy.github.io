from collections import deque
graph = [] ; dx = [-1,1,0,0] ; dy = [0,0,-1,1]
for _ in range(5):
    graph.append(list(map(int,input().split())))
s = set()
def dfs(x,y,num):
    if len(num) == 6:
        s.add(num)
        return
    for dir in range(4):
        nx,ny = x+dx[dir], y+dy[dir]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,num + str(graph[nx][ny]))
for i in range(5):
    for j in range(5):
        dfs(i,j,str(graph[i][j]))
print(len(s))

