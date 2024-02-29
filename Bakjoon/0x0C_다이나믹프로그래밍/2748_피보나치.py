N = int(input())
dp1 = [0]*91
dp1[0] = 0
dp1[1] = 1
dp1[2] = 1
for i in range(3,91):
     dp1[i] = dp1[i-1] + dp1[i-2]
print(dp1[N])