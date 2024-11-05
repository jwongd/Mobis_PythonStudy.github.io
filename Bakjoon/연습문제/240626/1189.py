import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
r,c,k = map(int,input().split())
graph =[]
for _ in range(r):
    tmp = list(input())
    graph.append(tmp)
cnt = 0
dx = [-1,1,0,0] ; dy = [0,0,-1,1]
vis = [[0]*(c+1) for _ in range(r+1)]
vis[r][0] = 1
def dfs(x,y,dist):
    global cnt
   # print(dist)
    if  x == 0 and y == c-1: #(0,c)-->집
       # print("dist:",dist)
        if dist == k:
            cnt+=1
            return
    for dir in range(4):
        nx, ny = x + dx[dir] , y+dy[dir]
        if 0<=nx<r and 0<=ny<c and vis[nx][ny] == 0 and graph[nx][ny] !='T':
            vis[nx][ny] = 1
            dfs(nx,ny,dist+1)
            vis[nx][ny] = 0
dfs(r,0,0)
print(cnt)

