n = int(input())
ans = 0
for _ in range(n):
    l = []
    s = list(input())
    if len(s)%2 !=0:
        continue
    for i in s:
        if l and i == l[-1]:
            l.pop()
            continue
        l.append(i)
    if len(l) == 0:
        ans += 1
print(ans)
