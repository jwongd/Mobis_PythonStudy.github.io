n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
ans  = 0
st , en = 0, arr[-1] - arr[0]
while st <= en:
    cnt = 1
    mid = (st + en) // 2 # 간격
    cur = arr[0]
    for i in arr:
        if i - cur >= mid : #간격보다 이전 ~ 현재 사이가 멀다면 추가 설치
            cnt += 1
            cur = i
    if cnt >= c:
        ans = mid
        st = mid + 1
    else:
        en = mid - 1
print(ans)