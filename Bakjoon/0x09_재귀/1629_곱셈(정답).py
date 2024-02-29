a,b,c = map(int,input().split())
def mul(a,n):
    if n == 1:
        return a%c
    else:
        tmp = mul(a,n//2)
        if n % 2 == 0:
            return (tmp*tmp) %c
        else:
            return (tmp*tmp*a)%c
ans = mul(a,b)
print(ans)

