import sys
input = sys.stdin.readline
n = int(input())
def my_round(v):
    if v - int(v) >= 0.5:
        return int(v)+ 1
    else:
        return int(v)
if n == 0:
    print(0)
    exit(0)
else:
    cut_cnt = my_round((0.15*n))
    #print("cut:",cut_cnt)
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    arr2 = arr[cut_cnt:(-cut_cnt)]
    if len(arr2) == 0:
        ans = my_round((sum(arr))/n)
    else:
        ans = my_round((sum(arr2))/len(arr2))
    print(ans)

    # print(*arr)
    # print(*arr2)