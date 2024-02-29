n = int(input())
for _ in range(n):
    ans = 0
    a,b = map(int,input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    print(*a_list)
    print(*b_list)
    for i in a_list:
        for j in b_list:
            if i>j:
                ans+=1
                # print((i,j))
            else:
                break
    print(ans)