n = int(input())
num = list(map(int,input().split()))
st =[]
ans = [-1]*n
idx = 0
for i in num:
    while st and st[-1][0]< i:
        x,y = st.pop()
        # ans.append(i)
        # print("idx:",idx)
        ans[y] = i
    st.append((i,idx))
    idx += 1
    #
    #
    # print("STACK")
    # print(*st)
    # print("ANSWER")
print(*ans)