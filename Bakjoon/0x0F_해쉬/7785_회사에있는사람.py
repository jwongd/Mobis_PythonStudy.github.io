n = int(input())
dict = {}
for _ in range(n):
    name, state = map(str,input().split())
    dict[name] = state
ans = []
for nm,st in dict.items():
    if st == 'enter':
        ans.append(nm)
ans.sort(reverse=True)
for i in ans:
    print(i)