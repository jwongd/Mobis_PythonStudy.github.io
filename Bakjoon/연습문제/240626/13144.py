import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
st = 0 ; en = 0  # sliding window?
tmp = [] ; ans = 0
for i in range(n):
    for j in range(i,n):
        tmp = arr[i:j]
        tmp2 = list(set(tmp))
        if tmp == tmp2:
            ans += 1
        else:
            break
print(ans)