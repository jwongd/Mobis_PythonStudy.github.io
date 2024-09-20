from collections import deque
from copy import deepcopy

dx = [1,0,-1,0] #남 동 북 서 (반시계방향)
dy = [0,1,0,-1]
direction ={
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}
def chk(x,y): #1: ok, 0: not ok
    return 0<=x<n and 0<=y<m

def move(x,y,dir,tmp):
    for d in dir:
        nx,ny = x,y
        while True:
            nx += dx[d]
            ny += dy[d]
            # out of range or meet the wall
            if chk(nx,ny) == 0 or tmp[nx][ny] == 6:
                break
            if tmp[nx][ny] != 0:
                continue
            tmp[nx][ny] = '#'
def zero_cnt(tmp):
    global cnt
    mn = 0
    for i in tmp:
        mn += i.count(0)
    cnt = min(cnt,mn)
def dfs(depth,board): #deepcopy쓰면 시간손해 큼..
    #직전 상태 저장
    tmp = [[j for j in board[i]] for i in range(n)]
    if depth == len(cctv):
        zero_cnt(tmp)
        return
    x,y,num = cctv[depth]
    for d in direction[num]:
        move(x,y,d,tmp)
        dfs(depth+1,tmp) # backtracking
        tmp = [[j for j in board[i]] for i in range(n)] #직전상태로 변경
graph = [] ; cctv = []
n, m = map(int, input().split())
cnt = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] in range(1,6):
            cctv.append((i,j,graph[i][j])) # x, y, 종류
        if graph[i][j] == 0: cnt+=1
dfs(0,graph)
print(cnt)








