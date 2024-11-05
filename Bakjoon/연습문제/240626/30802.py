n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
ans1 = 0
for i in arr:
    # print("---------------------")
    # print("i:",i)
    if i%a == 0:
        ans1+= (i//a)
    else:
        ans1 += (i//a) + 1
    # print("ans:",ans1)
print(ans1)
ans2 = (divmod(n,b))
print(*ans2)
