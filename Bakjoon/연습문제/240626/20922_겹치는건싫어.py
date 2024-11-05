from collections import Counter
n,k = map(int,input().split())

arr = list(map(int,input().split()))
if n == 1:
    print(1)
    exit(0)
st = 0; en = 1 ; mx = -1
while st < en:
    a = arr[st:en+1]
    mx = max(mx,len(a))
    c = Counter(a)
    for i,j in c.items():
        while j <= k:
            c[st] -= 1
            st += 1



