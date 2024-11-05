n,k = map(int,input().split())
arr = list(map(int,input().split()))
# if k == 1:
#     print(max(arr))
#     exit(0)
s = 0
arr_sum = [0]*len(arr)
arr_sum[0] = sum(arr[0:k])
mx = arr_sum[0]
for i in range(1,len(arr)-k+1):
    arr_sum[i] = arr_sum[i-1] - arr[i-1] + arr[i+k-1]
    mx = max(mx,arr_sum[i])
print(mx)