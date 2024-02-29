from collections import deque

F,S,G,U,D = map(int,input().split())
dx = [U,-D]
board = [0]*(F+1)
q = deque()
q.append(S)
board[S] = 1
while q:
    x = q.popleft()
    for dir in range(2):
        nx = x + dx[dir]
        if 1<=nx<=F and board[nx]==0 : #1층부터 있다는 사실을 유념!
            board[nx] = board[x] + 1
            q.append(nx)
if(board[G]==0):
    print("use the stairs")
else:
    print(board[G]-1)
