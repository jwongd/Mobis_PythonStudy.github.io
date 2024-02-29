s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
ans = [0]*len(al)
for i in s:
    for j in range(len(al)):
        if i == al[j]:
            ans[j]+=1
print(*ans)

