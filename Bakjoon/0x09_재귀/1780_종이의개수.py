N = int(input())
l =[]
ans_1 = 0
ans_0 = 0
ans_m1 = 0
for _ in range(N):
    l.append(list(map(int,input().split())))
def chk(x,y,n):
    global ans_1,ans_0,ans_m1
    flag = 0
    if n == 0:
        return
    first = l[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != l[i][j]:
                flag = 1
                break
    if flag == 1:
        n = n//3
        for i in range(3):
            for j in range(3):
                chk(x+i*n,y+j*n,n)
    else:
        if first == 1:
            ans_1 += 1
        elif first == 0:
            ans_0 += 1
        else:
            ans_m1 +=1
chk(0,0,N)
print(ans_m1,ans_0,ans_1)