from collections import deque
dx = [-1,1,0,0] ; dy= [0,0,-1,1]
t = int(input())
def bfs(board):
    vis = [[-1]*len(board[0]) for _ in range(len(board))]
    visf = [[-1] * len(board[0]) for _ in range(len(board))]
    w = len(board[0]) ; h = len(board)
    q = deque() ; q2 = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '@':
                q.append((i,j))
                vis[i][j] = 0
            if board[i][j] == '*':
                q2.append((i,j))
                visf[i][j] = 0
    while q2: #fire bfs
        x,y = q2.popleft()
        for dir in range(4):
            nx , ny = x + dx[dir], y + dy[dir]
            if 0<=nx<h and 0<=ny < w:
                if visf[nx][ny] == -1 and board[nx][ny] != '#':
                    visf[nx][ny] = visf[x][y] + 1
                    q2.append((nx,ny))
    #print(*visf)
    #print(*vis)
    while q: # man bfs
        x,y = q.popleft()
        #print("x:",x,"y:",y,"bd:",board[x][y],"dist:",vis[x][y])
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <=nx <h and 0 <=ny <w:
                if vis[nx][ny] == -1 and board[nx][ny] == '.' :
                    if visf[nx][ny] == -1 :
                        vis[nx][ny] = vis[x][y] + 1
                        q.append((nx, ny))
                    else:
                        if vis[x][y]+1 < visf[nx][ny]:
                            vis[nx][ny] = vis[x][y] + 1
                            q.append((nx, ny))

            else: #탈출 성공
                return vis[x][y] + 1
    return "IMPOSSIBLE"
for _ in range(t):
    w,h = map(int,input().split())
    board = [list(map(str,input())) for _ in range(h)]
    print(bfs(board))

# 1
# 10 5
# ##########
# #@....#*.#
# #.....#..#
# #.....#..#
# ##.#######