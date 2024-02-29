N = int(input())
d = [0]*(N+1)
a = [0]*(N+1)
ans = []
for i in range(2,N+1):
    d[i] = d[i-1] + 1
    a[i] = i-1
    if i%2 == 0 :
        if d[i] > d[i//2]+1:
            a[i] = i//2
        d[i] = min(d[i],d[i//2]+1)

    if i%3 == 0 :
        if d[i] > d[i//3]+1:
            a[i] =  i//3
        d[i] = min(d[i], d[i//3] + 1)
cnt = N
ans.append(N)
while(True):
    if cnt == 1:
        break
    ans.append(a[cnt])
    cnt = a[cnt]
print(d[N])
print(*ans)
