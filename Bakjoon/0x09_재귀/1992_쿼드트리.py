N = int(input())
l = []
real_ans = ''
for _ in range(N):
    l.append(list(map(int,input())))
def d(x,y,n):
    global real_ans
    flag = 0
    # real_ans += '('
    if n == 0:
        return
    first = l[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != l[i][j]:
                flag = 1
                break
    if flag == 1:
        n = n//2
        real_ans+='('
        d(x,y,n)
        d(x, y + n, n)
        d(x+n,y,n)
        d(x + n, y+n, n)
        real_ans+=')'
    else: #모두가 같음
        real_ans += str(first)
d(0,0,N)
print(real_ans)