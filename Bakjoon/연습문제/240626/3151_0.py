import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))
ans = 0
for i in range(len(arr)-2):
    st = i+1
    en = len(arr) - 1
    while st < en:
        if st == i :
            st += 1
            continue
        if arr[st] + arr[i] + arr[en] == 0:
            print("i:",i,"st:",st,"en:",en)
            print((arr[st], arr[i], arr[en]))
            ans += 1
            st += 1
        elif arr[st] + arr[i] + arr[en] > 0:
            en -= 1
        else: # arr 합이 <0
            st += 1
print(ans)
