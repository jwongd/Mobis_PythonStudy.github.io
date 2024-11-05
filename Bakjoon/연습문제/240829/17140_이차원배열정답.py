from collections import Counter
from functools import reduce
#R 연산
def R(arr):
    mx = 0
    for i in range(len(arr)):
        x = Counter(arr[i])
        del x[0]
        x = list(x.items())
        x.sort(key = lambda x: (x[1],x[0]))
        if len(x) > 50 : x = x[:50]
        arr[i] = reduce(lambda x,y : list(x)+list(y),x[1:], list(x[0]))
        mx = max(mx,len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) < mx:
            arr[i].extend([0]*(mx-len(arr[i])))
r,c,k = map(int,input().split())
r,c = r-1,c-1
board = [list(map(int,input().split())) for _ in range(3)]
time = 0
if r<len(board) and c<len(board[0]) :
    if board[r][c] == k:
        print(time)
        exit(0)
while True:
    if len(board) >= len(board[0]): # 행의개수 >= 열의개수 --> R연산
        R(board)
    else:
        board = list(map(list,zip(*board))) # transpose
        R(board)
        board = list(map(list, zip(*board))) # transpose
    time += 1
    if time > 100 :
        print(-1)
        break
    if r < len(board) and c < len(board[0]):
        if board[r][c] == k :
             print(time)
             exit(0)