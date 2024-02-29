n,target = list(map(int,input().split()))
bar =[]
for _ in range(n):
    bar.append(int(input()))
st = 1
en = max(bar)
while st <= en:
    s = 0
    mid = (st+en)//2
    for i in bar:
        s += i//mid
    if s >=target:
        st = mid + 1
    else:
        en = mid-1
print(en)