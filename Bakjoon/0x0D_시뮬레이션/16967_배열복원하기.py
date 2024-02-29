h,w,x,y = list(map(int,input().split()))
b = []
for _ in range(h+x):
    b.append(list(map(int,(input().split()))))
a = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]
for i in range(x,h):
    for j in range(y,w):
        a[i][j] = b[i][j] - a[i-x][j-y]
for i in range(h):
    for j in range(w):
        print(a[i][j],end=" ")
    print("")