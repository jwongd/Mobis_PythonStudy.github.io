from collections import Counter
N = int(input())
arr =[]
for _ in range(N):
    arr.append(int(input()))
arr = sorted(arr)
x = Counter(arr).most_common()
print(x[0][0])
