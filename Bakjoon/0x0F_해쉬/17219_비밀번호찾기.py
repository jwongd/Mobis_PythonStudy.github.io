n,m = map(int,input().split())
x = []
password = {}
for _ in range(n):
    l = list(map(str,input().split()))
    password[l[0]] = l[1]
for _ in range(m):
    a = input()
    b = password[a]
    x.append(b)
for i in x:
    print(i)



