dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]
from collections import deque
n,m, k = map(int,input().split())
arr = [] ; origin = []
tree = [] ; die = deque();tree2=[]
br = []
for _ in range(n):
    origin.append(list(map(int,input().split())))
for _ in range(m):
    a,b,c = map(int,input().split())
    tree.append((a-1,b-1,c)) # a,b -> location, c -> age
arr = origin
def spring():
    global die
    die = []
    tree.sort(key = lambda x: x[2])
    print(*tree)
    for _ in range(len(tree)):
        x,y,age = tree.pop()
        if arr[x][y] >= age :
            arr[x][y] -= age
            tree2.append((x,y,age+1))
        else:
            die.append((x,y,age//2))
    return
def summer():
    while die:
        x,y,age = die.pop()
        arr[x][y] += age
    return
def chk_range(x,y):
    if 0<=x<n and 0<=y<m:
        return 1
    return 0
def fall():
    for i in tree2:
        x,y = i[0],i[1]
        if i[2] % 5 == 0:
            for dir in range(8):
                nx,ny = x+dx[dir],y+dy[dir]
                if chk_range(nx,ny):
                    tree2.append((nx,ny,1))

    return
def winter():
    for i in range(n):
        for j in range(m):
            arr[i][j] += origin[i][j]
    return tree2
for _ in range(k):
    print("------")
    spring()
    #print(*tree2)
    summer()
    fall()
    tree = winter()
    print(*tree)
ans = 0
for i in range(n):
    for j in range(n):
        print(tree[i][j])
        # ans += len(tree[i][j])
print(ans)

