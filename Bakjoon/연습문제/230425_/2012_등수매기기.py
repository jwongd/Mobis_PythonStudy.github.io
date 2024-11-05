n = int(input())
a = []
cnt = 0
for _ in range(n):
    a.append(int(input()))
a.sort()
for i in range(n):
    cnt += abs((i+1)-a[i])
print(cnt)