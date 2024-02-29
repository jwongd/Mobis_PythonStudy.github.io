n = int(input())
height = []
st = []
ans = 0
for _ in range(n):
    height.append(int(input()))
for i in height:
    while st and st[-1]<=i:
        st.pop()
        if len(st) == 0:
            ans+=1
    print("STACK")
    print(*st)
    st.append(i)
ans += (n-1)
# print(ans)
#2140 5692 5405 2119

