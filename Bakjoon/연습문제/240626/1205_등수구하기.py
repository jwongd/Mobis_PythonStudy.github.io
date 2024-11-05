from bisect import bisect_left,bisect_right
n,new_score,p = map(int,input().split())
if n == 0:
    print(1)
    exit(0)
arr = list(map(int,input().split()))
arr = arr[::-1]
# print(*arr)
a = bisect_left(arr,new_score)
b = bisect_right(arr,new_score)
# print(a,b)
if n-a == p:
    print(-1)
else:
    print(len(arr)+1-b)
