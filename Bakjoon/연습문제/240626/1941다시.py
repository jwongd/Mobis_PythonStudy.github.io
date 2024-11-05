from itertools import combinations as cb
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
graph =[list(input().strip()) for _ in range(5)]
l = []
for i in range(5):
    for j in range(5):
        l.append((i,j))
c = list(cb(l,7))
dx = [-1,1,0,0] ; dy = [0,0,-1,1]
def chk_seven(list_,cnt):
    q = deque()
    vis = [[0]*5 for _ in range(5)]
    for i,j in list_:
        vis[i][j] = 1
        q.append((i,j))
        while q:
            x,y = q.popleft()
            for dir in range(4):
                nx,ny = x + dx[dir], y + dy[dir]
                if 0<=nx<5 and 0<=ny<5:
                    if vis[nx][ny] == 0 and (nx,ny) in list_:
                        cnt += 1
                        q.append((nx,ny))
                        vis[nx][ny] = 1
    #return cnt
    if cnt == 7 : return True
    else: return False
# print(chk_seven(c[0],1))
def chk_num(list_):
    cnt = 0
    for i,j in list_:
        if graph[i][j] == 'S' :
            cnt += 1
        else:
            cnt -= 1
    if cnt > 0 : return True
    else: return False
ans = 0
for i in c:
    if chk_num(i) and chk_seven(i,1):
        ans += 1
print(ans)
    #function : 'S' 7개 연속인지?
    #25C7


