import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
arr.sort(reverse= True)
for i in arr:
    print(i)