from itertools import combinations_with_replacement as cb
N,M = map(int,input().split())
l = sorted(list(map(int,input().split())))
ans = set()
for i in cb(l,M):
    ans.add(i)
ans = sorted(list(ans))
for i in ans:
    for j in i:
        print(j,end=" ")
    print()