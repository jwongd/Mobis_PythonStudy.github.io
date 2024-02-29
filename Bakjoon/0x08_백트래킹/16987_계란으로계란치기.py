from itertools import permutations as pm
import copy
N = int(input())
egg =[]
for i in range(N):
    x, y = map(int,input().split())
    egg.append([x,y])

for i in range(N):
    print("====================")
    x = list(pm(egg[i+1:],N-1-i))
    for hp,strong in x:
        print(hp,strong)

