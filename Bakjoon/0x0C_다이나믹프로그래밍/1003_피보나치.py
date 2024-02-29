T = int(input())
dp1 = [0]*41
dp2 = [0]*41
dp1[0] = 1
dp1[1] = 0
dp1[2] = 1
dp2[0] = 0
dp2[1] = 1
dp2[2] = 1
for i in range(3,41):
     dp1[i] = dp1[i-1] + dp1[i-2]
     dp2[i] = dp2[i - 1] + dp2[i - 2]
for _ in range(T):
    N = int(input())
    print(dp1[N],dp2[N])