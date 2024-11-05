from bisect import bisect_left
from collections import deque
p = int(input())
for _ in range(p):
    n, *arr = map(int,input().split())
    arr = list(arr)

    arr_s = sorted(arr)
    ans = 0
    #print(arr)
   # print(arr_s)
    arr = deque(arr)
    for i in range(19,-1,-1):
       # print("===================")
        x = arr[i]
        print("x:",x)
        position = bisect_left(arr,x)
        print("position:",position,"distance:",19-position)
        arr.insert(position,x)
      #  print(*arr)
        ans+=(19-position)


    print(ans)
