n,m = map(int,input().split()) #나무의수/ 나무의길이 목표
tree = list(map(int,input().split()))
tree = sorted(tree,reverse=True)
st = 1
en = max(tree)
while st <= en:
    mid = (st+en)//2
    s = 0
    for i in tree:
        if (i-mid) > 0 :
            s += (i - mid)
        if s>m:
            break
    if s>=m:
        st = mid+1
    else:
        en = mid-1
print(en)