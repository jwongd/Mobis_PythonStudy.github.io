n,p,q = map(int,input().split())
d1 = {i:int(i//p) for i in range(1,n+1)}
d2 = {i:int(i//q) for i in range(1,n+1)}
ans = [0]*(n+1)
ans[0] = 1 #A0
for i in range(1,n+1):
    ans[i] = ans[d1[i]] + ans[d2[i]]
print(ans[n])

