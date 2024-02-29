from collections import deque
n = int(input())
q = []
i = 0
arr = deque()
ans = []
for _ in range(n):
    arr.append(int(input()))
#arr : 입력된 수열
while(i<=n): # 1부터 순회
    while(q and q[-1] == arr[0]):
        q.pop()
        arr.popleft()
        ans.append("-")
    if i == n: break
    q.append(i+1) # 1,2,3,..
    ans.append("+")
    i += 1
if q :
    print("NO")
else:
    for i in ans:
        print(i)