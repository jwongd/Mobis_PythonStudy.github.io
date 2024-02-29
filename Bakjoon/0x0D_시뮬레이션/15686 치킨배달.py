from itertools import combinations as cb
n,m = map(int,input().split())
graph = []
chicken_spot = []
house = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
# print(*graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_spot.append([i,j])
        if graph[i][j] == 1:
            house.append([i,j])
x = list(cb(chicken_spot,m))
fin = 1e9
for cblist in x:
    print(cblist)
    ans = 0
    tmp = 0
    for x,y in house:
        mn = 1e9
        # print("===========")
        for i in range(len(cblist)):
            print(cblist[i])
            tmp = abs(cblist[i][0]-x) + abs(cblist[i][1]-y)
            # print("tmp:",tmp)
            mn = min(mn, tmp)
        ans += mn
    fin = min(ans,fin)
print(fin)