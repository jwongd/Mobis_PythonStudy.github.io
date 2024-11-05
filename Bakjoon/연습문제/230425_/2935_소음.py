sq = [i*i for i in range(1,10001)]
ans = []
m = int(input())
n = int(input())
for i in sq:
    if m<=i<=n:
        ans.append(i)
if len(ans)!=0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)