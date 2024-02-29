n = int(input())
k = int(input()) #count of apples
dx = [0,1,0,-1]
dy = [1,0,-1,0]
rotat = {}
# right rotate : index ++ // left rotate : index --
cnt = 1
graph = [[0]*(n) for _ in range(n)] #map
idx = 0
for _ in range(k):
    a , b = map(int,input().split())
    graph[a-1][b-1] = 1
l = int(input())
for _ in range(l):
    a1, b1 = map(str,input().split())
    a1 = int(a1)
    rotat[a1] = b1
snake = [(0,0)]
nx = 0
ny = 0
while True:
    nx = nx + dx[idx]
    ny = ny + dy[idx]
    if (nx>=n or ny>=n or (nx,ny) in snake or nx<0 or ny<0):
        ans = cnt
        break
    snake.append((nx, ny))
    if graph[nx][ny]== 0: #지금 필드에 사과가 있는게 아니라면
        snake.pop(0)
    else:
        graph[nx][ny] = 0
    if cnt in rotat.keys():
        if rotat[cnt] == 'D': #right rotate
            idx = (idx+1) % 4
        elif rotat[cnt] == 'L': #left rotate
            idx = (idx-1) % 4
    cnt += 1

print(ans)