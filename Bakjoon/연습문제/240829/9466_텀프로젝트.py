import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    pick = [0] + list(map(int,input().split()))
    vis = [0] * (n+1)
    for i in range(1,n+1):
        if vis[i] == 0:
            num = i
           # print("i:",i)
            while vis[i] == 0:
                vis[i] = num
                i = pick[i]
            #print(*vis)
            while vis[i] == num:
                vis[i] = -1
                i = pick[i]
            #print(*vis)
    ans = n - vis.count(-1)
    print(ans)




