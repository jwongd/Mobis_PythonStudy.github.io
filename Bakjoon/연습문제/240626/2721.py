t = int(input())
def tttt(n):
    return n*(n+1)/2
for _ in range(t):
    ans = 0
    n = int(input())
    for i in range(1,n+1):
        ans+= i*tttt(i+1)
    print(int(ans))