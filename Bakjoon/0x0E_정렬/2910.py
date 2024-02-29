from collections import Counter
n,c = map(int,input().split())
num = list(map(int,input().split()))
c = Counter(num).most_common()
ans = []
for i,j in c:
    for _ in range(j):
        ans.append(i)
print(*ans)