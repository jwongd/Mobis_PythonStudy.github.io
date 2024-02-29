cnt_Y = 0
cnt_S = 0
ans = 0
l = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(5):
    l.append(list(input()))
def princess(cur,x,y):
    global cnt_Y,cnt_S,ans # S : 다솜, Y: 도연
    if cur == 7:
        if cnt_S > cnt_Y :
            ans+=1
        return
    if cnt_Y >= 4:
        return
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or vis[nx][ny]:
            return
        if l[nx][ny] == 'S':
            cnt_S += 1
        if l[nx][ny] == 'Y':
            cnt_Y += 1
        vis[nx][ny] = 1
        princess(cur+1,nx,ny)
        if l[nx][ny] == 'S':
            cnt_S -= 1
        if l[nx][ny] == 'Y':
            cnt_Y -= 1
        vis[nx][ny] = 0


for i in range(5):
    for j in range(5):
        vis = [[0]*5 for _ in range(5)]
        if l[i][j] == 'S':
            cnt_S = 1
        if l[i][j] == 'Y':
            cnt_Y = 1
        vis[i][j] = 1
        princess(1, i, j)
print(ans)