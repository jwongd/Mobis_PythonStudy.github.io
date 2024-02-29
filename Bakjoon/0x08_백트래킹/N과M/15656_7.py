from itertools import product as pd
N,M = map(int,input().split())
l = sorted(list(map(int,input().split())))
for i in pd(l,repeat = M):
    for j in i:
        print(j,end=" ")
    print()