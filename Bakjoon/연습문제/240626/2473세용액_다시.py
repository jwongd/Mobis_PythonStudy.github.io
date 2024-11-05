n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = []
mx = int(1e12)
#print(*arr)
for i in range(n-1): # start 용액 지정
    st = i+1 # i 바로 다음
    en = n-1 # 맨 뒤
   # print("=======")
    while st < en:
        mid = arr[i] + arr[st] + arr[en]
       # print("st:", st,"mid:",mid,"en:",en )
        if mid == 0:
            ans = [arr[i],arr[st],arr[en]]
            break
        else:
            if abs(mx) > abs(mid):
                ans = [arr[i],arr[st],arr[en]]
                mx = mid
               # print(*ans)
            if mid > 0:
                en -= 1
            else: # mid < 0
                st += 1
print(*ans)
