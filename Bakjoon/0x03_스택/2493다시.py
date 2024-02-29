n = int(input())
num = list(map(int,input().split()))
st =[]
ans =[0]*(n)
for i in range(n):
    while st :
        if st[-1][1] > num[i]:
            ans[i] = st[-1][0] + 1
            break
        st.pop()
    st.append([i,num[i]])
print(*ans)