import sys
input = sys.stdin.readline
N = int(input())
ans = [['*']*N for _ in range(N)]

def d(x,y,n):
    global ans
    if n == 1:
        return
    for i in range(x,n+x):
        for j in range(y,y+n):
            if n//3 + x<= i < (n//3)*2 + x and n//3 + y<= j < (n//3)*2 + y :
                ans[i][j] = ' '
    n = n//3
    for i in range(3):
        for j in range(3):
            d(x+n*i,y+n*j,n)


d(0,0,N)
result = '\n'.join(''.join(row) for row in ans)
print(result)