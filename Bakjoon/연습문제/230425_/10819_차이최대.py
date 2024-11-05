from itertools import  combinations as cb
n = int(input())
a = list(map(int,input().split()))
a.sort()
sum = 0
for i in range(n):
    sum += abs(a[i] - a[n-i-1])
print(sum)



