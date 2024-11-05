n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
print(*arr)

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
