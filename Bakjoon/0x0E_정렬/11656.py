s = (input())
ans = []
for i in range(len(s)):
    ans.append(s[i:])
ans.sort()
print(*ans)
