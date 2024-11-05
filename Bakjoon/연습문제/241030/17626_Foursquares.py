n = int(input())
dp = [0] * (50001) # dp[i] 는 제곱수로 만들수있는 거의 개수
sq = [i*i for i in range(1,100)]
for i in range(1,n+1):
    if i in sq:
        dp[i] = 1
flag = 0
for i in range(1,n+1):
    for j in range(1,i): # 1~ i-1
        flag = 0
        if flag == 1:

            break
        if dp[i-j] != 0 or dp[j]!= 0:
            if i ==3 :
                print("i:",i,"j:",j)
            dp[i] = dp[i-j] + dp[j] # dp[6] = dp[1] + dp[5]
            flag = 1
for i in range(1,n+1):
    print(dp[i])


