from itertools import permutations as pm
import sys
input = sys.stdin.readline
n = int(input())
ans = []
p = [i for i in range(1,n+1)]
arr = list(map(int,input().split()))
# 10으로 N이작음 --> 모든 경우의 수 따져서 만족하는 놈 있으면 그거 픽
for case in pm(range(1,n+1),n):
    #print("--------")
   # print(case)
    arr2 = [0] * (n)
    flag = 0
    for i2 in range(n):
        for j2 in range(0,i2):
            if case[j2] > case[i2]:
                arr2[i2] += 1
    # print(*case)
    # print(*arr2)
    case2 = list(zip(case,arr2))
    case2.sort(key = lambda x : x[0])
    # print(*case2)
    case3 = [0]*n
    for i in range(n):
        case3[i] = case2[i][1]
    # print(*case3)
    # 2 1 3 4
    for i in range(n):
        if case2[i][1] != arr[i]:
            flag = 1
            break
    if flag == 0:
        ans = case
print(*ans)


