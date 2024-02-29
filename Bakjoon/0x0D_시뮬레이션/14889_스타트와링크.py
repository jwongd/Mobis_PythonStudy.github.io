from itertools import combinations as cb
N = int(input())
M = N//2
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
a = [i for i in range(N)]
mn = 1e9

for i in cb(a,M):
    sum = 0
    b = []
    for x in a:
        if x not in i:
            b.append(x)
    for j1, j2 in cb(i,2):
        sum += (graph[j1][j2] + graph[j2][j1])
    for j3, j4 in cb(b,2):
        sum -= (graph[j3][j4] + graph[j4][j3])
    sum = abs(sum)
    mn = min(mn,sum)
print(mn)