n,l = map(int,input().split())
# 홀수 : n = length * 가운데 수
# 짝수 : n = (가운데 두 수의 합)  * (length // 2)
ans = []
for i in range(l,101):
    # i = length
    if i % 2 != 0:
        if (n/i == n//i):
            mid = n//i
            ans.append(mid)
    while True:
        if mid - i < 0 or mid + i > int(1e9) :
            break
        ans.append(mid-i)
        ans.append(mid+i)
        


    else:
        i2 = i//2
        if (n/i2)%2 != 0:
            mid1 = n/(i2*2)
            mid2 = mid1 + 1


