n = int(input())
b = []
c = 0
def sudm(n):
    a = []
    i = 1
    while True:
        if n % i == 0:
            a.append(i)
            a.append(int(n/i))
        if i*i >= n :
            break
        i += 1
    a = list(set(a))
    a.sort()
    return(sum(a))

for i in range(1,n+1):
    c += sudm(i)
print(c)