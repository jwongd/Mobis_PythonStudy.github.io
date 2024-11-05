# a^b mod c = a^(b/2) mod c  * a^(b/2) mod c * a mod c (b가 홀수)
# a^b mod c = a^(b/2) mod c * a^(b/2) modc  (b가 짝수)
def mul(a,b):
    if b == 1:
        return a%c
    tmp = mul(a,b//2)%c
    if b%2 == 0: #짝수
        return (tmp*tmp)%c
    else: #홀수
        return (tmp*tmp*a)%c
a,b,c = map(int,input().split())
print(mul(a,b))