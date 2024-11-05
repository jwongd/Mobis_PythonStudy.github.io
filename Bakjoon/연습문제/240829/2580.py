def row(x,v):
    for j in range(9):
        if graph[x][j] == v:
            return False
    return True

def col (y,v):
    for i in range(9):
        if graph[i][y] == v:
            return False
    return True
def diag(x,y,v):
    for i in range(9):
        for j in range(9):
            if abs(x-i) == abs(y-j):
                return False
    return True
def dfs(depth):
    if depth == 8:
        return
    x,y = zero[depth]
    for num in range(1,10):
        if row(x,num) and col(y,num) and diag(x,y,num):
            graph[x][y] = num
            dfs(depth+1)
            graph[x][y] = 0



graph = []
for _ in range(9):
    graph.append(list(map(int,input().split())))
zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i,j))
dfs(0)
print(*graph)