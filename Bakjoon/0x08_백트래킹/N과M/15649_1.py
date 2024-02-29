from itertools import permutations as pm
N,M = map(int,input().split())
ans = []
l = [i for i in range(1,N+1)]
for i in pm(l,M):
    for j in i:
        print(j,end=" ")
    print()
