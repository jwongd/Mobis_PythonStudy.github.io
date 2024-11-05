dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,2,1,-1,-2]
moves = []
N = 6
vis = [[0]*N for _ in range(N)]
for _ in range(36):
    a = input().strip()
    x = ord(a[0]) - ord('A')
    y = int(a[1]) - 1
    moves.append((x,y))
start_x, start_y = moves[0]
x,y = start_x,start_y
vis[x][y] = 1

def valid_move(x1,y1,x2,y2):
    for dir in range(8):
        if x + dx[dir] == x2 and y1 + dy[dir] == y2:
            return True
    return False
valid = True
for i in range(1,36):
    next_x, next_y = moves[i]
    if not valid_move(x,y,next_x,next_y) or vis[next_x][next_y] == 1:
        valid = False
        break
    x,y = next_x , next_y
    vis[x][y] = 1
if valid and valid_move(x,y,start_x,start_y):
    print("Valid")
else:
    print("Invalid")

