from itertools import chain
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

g = list(chain(*graph))
#print(*g)
g = sorted(g,reverse=True)
print(g[n-1])