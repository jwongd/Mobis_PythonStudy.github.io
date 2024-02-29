from itertools import permutations as pm
N,M = map(int,input().split())
l = sorted(list(map(int,input().split())))
for i in pm(l,M):
    for j in i:
        print(j,end=" ")
    print()