import heapq
import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in tmp:
        heapq.heappush(graph,i)
print(heapq.nlargest(n,graph)[-1])