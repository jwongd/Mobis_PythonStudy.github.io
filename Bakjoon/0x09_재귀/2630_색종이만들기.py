N = int(input())
white = 0
blue = 0
l = []
for i in range(N):
    l.append(list(map(int,input().split())))
def chk(x,y,n):
    global white, blue
    flag = 0
    if n == 0:
        return
    first = l[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != l[i][j]:
                flag = 1
                break
    if flag == 1:
        n = n//2
        chk(x+n,y,n)
        chk(x,y+n,n)
        chk(x,y,n)
        chk(x+n,y+n,n)
    else:
        if first == 0 :
            white += 1
        else:
            blue += 1
chk(0,0,N)
print(white)
print(blue)