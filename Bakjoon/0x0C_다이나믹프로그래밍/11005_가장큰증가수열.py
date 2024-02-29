n = int(input())
num = list(map(int,input().split()))
dp = num[:] #복사하는 방법
for i in range(len(num)):
    for j in range(i):
        if num[i]>num[j] : # i번째 즉 지금 보고있는 숫자가 제일 클 때
            dp[i] = max(dp[j] + num[i], dp[i]) #dp : 가장 큰 증가부분수열의 합
print(max(dp))
