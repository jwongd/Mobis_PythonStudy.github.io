from itertools import combinations as cb
N,M = map(int,input().split())
l = sorted(list(map(int,input().split())))
for i in cb(l,M):
    for j in i:
        print(j,end=" ")
    print()