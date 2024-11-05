import sys
input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    arr = input().split()
    order = arr[0]
    if order == 'add':
        if arr[1] not in s:
            s.add(arr[1])
    elif order == 'remove':
        if arr[1] in s:
            s.remove(arr[1])
    elif order == 'check':
        if arr[1] in s:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if arr[1] in s:
            s.remove(arr[1])
        else:
            s.add(arr[1])
    elif order == 'all':
        s = set()
        for i in range(1,21):
            s.add(str(i))
    elif order == 'empty':
        s = set()
