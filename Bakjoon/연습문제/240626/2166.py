n = int(input())
points = []
for _ in range(n):
    a,b = map(int,input().split())
    points.append((a,b))
area1 , area2 =  0,0
for i in range(n-1):
    x = (points[i][0] * points[i+1][1])
    area1 += x
for i in range(n-1):
    y = (points[i+1][0] * points[i][1])
    area2 += y
#xny1- x1yn
area1 += points[n-1][0]* points[0][1]
area2 += points[0][0] * points[n-1][1]
ans = abs(area1 - area2 )/2
print(ans)
