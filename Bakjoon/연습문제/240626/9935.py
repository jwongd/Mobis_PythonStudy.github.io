import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
l = len(b)

st = []
for i in range(len(a)):
    st.append(a[i])
    if len(st) >= l and ''.join(st[-l:]) == b:
        for _ in range(l):
            st.pop()

ans = ''.join(st)
if not st:
    print("FRULA")
else:
    print(ans)