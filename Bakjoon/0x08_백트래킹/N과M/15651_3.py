from itertools import product as pd
N,M = map(int,input().split())
l = [i for i in range(1,N+1)]
for i in pd(l,repeat = M):
    for j in i:
        print(j,end= " ")
    print()
