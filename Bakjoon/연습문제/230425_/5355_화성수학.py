t = int(input())
for _ in range(t):
    num = list(map(str,input().split()))
    ans = 0
    for i in range(len(num)):
        if i ==0:
            ans += float(num[i])
        else:
            if num[i] == '#':
                ans -= 7
            elif num[i] == '%':
                ans += 5
            elif num[i] == '@':
                ans *= 3
    print("%0.2f" %ans)
