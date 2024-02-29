import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x = (input().strip())
    arr.append(x)
def sumnum(x):
    y = 0
    for i in x:
        if i.isdigit():
            y+= int(i)
    return y
arr.sort(key = lambda x: (len(x),sumnum(x),x))
for i in arr:
    print(i)