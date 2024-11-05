import sys
input = sys.stdin.readline
n = int(input())
st = [] ; ans = 0
for i in range(n):
    x = int(input())
    while st and st[-1] <= x:
        st.pop()
    st.append(x)
    print(*st)
print(ans)
