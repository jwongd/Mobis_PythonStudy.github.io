t = int(input())
for _ in range(t):
    s= {}
    p = int(input())
    for _ in range(p):
        a,b = map(str,input().split())
        a = int(a)
        s[b] = a #선수 - 가격
        sorted(s ,key= lambda x: x[1])
        print(s.items())


