import sys
input = sys.stdin.readline
n,m = map(int,input().split())
pm = {}
for i in range(1,n+1):
    a = input().rstrip()
    pm[i] = a
    pm[a] = i
for j in range(m):
    s = input().rstrip()
    if s.isdigit() == True:
        ans = pm[int(s)]
        print(ans)
    else:
        ans = pm[s]
        print(ans)
