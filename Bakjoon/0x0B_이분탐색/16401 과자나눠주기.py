m,n = map(int,input().split()) #조카, 과자
num = list(map(int,input().split()))
st = 1
en = max(num)
while st<=en:
    mid = (st+en)//2
    s = 0
    for i in num:
        s += i//mid
    if s >= m:
        st = mid + 1
    else:
        en = mid - 1
print(en)
