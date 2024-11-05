n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    c = a+b
    for d in range(50,0,-1):
        if c != d:
            print(d)
            break
