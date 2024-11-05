from itertools import permutations as pm
n = int(input())
arr = [i for i in range(1,n+1)]
for i in pm(arr,n):
    print(*i)