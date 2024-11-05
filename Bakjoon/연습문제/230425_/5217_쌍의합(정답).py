t = int(input())
for _ in range(t):
    n = int(input())
    start = 1
    print(f"Pairs for {n}: ", end='')
    b = []
    for k in range((n-1)//2):
        if k!=0:
            print(',',end = ' ')
        print(start,n-start,end='')
        start += 1
    print()


