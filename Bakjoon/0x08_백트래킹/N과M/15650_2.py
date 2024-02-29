from itertools import combinations as cb
N,M = map(int,input().split())
l = [i for i in range(1,N+1)]
for i in cb(l,M):
    for j in i:
        print(j,end= " ")
    print()
