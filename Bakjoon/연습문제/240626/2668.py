from itertools import combinations as cb
from collections import deque
n = int(input())
from collections import defaultdict
arr1 = [i for i in range(1,n+1)]
arr2 = defaultdict(list)
ans2 = []; vis = [0] * (n+1)
same= 0
for idx in range(1,n+1):
    x = int(input())
    #print("idx:",idx,"x:",x)
    if idx == x:
        vis[x] = 1
        same += 1
        ans2.append(x)
        continue
    arr2[idx].append(x)
ans_len = same
#print(ans_len)
#print(arr2)
# 1개씩 뽑았을 때 --> 2개씩 뽑았을 때 --> 3개씩 뽑았을 때 --> n개모두 뽑았을때
# nC1  + nC2 + ... nCn = 2^n = n이 100일 때 10^30이므로 말도안되는 풀이법...
# arr1 ==> 인덱스와 숫자가 일치함
# arr2에서 graph[idx] = val로 할 때 뭔가 순환고리를 찾으면 될 거같음
#--> 가장 긴 순환고리를 찾아주세요! --> 토끼와 거북이 알고리즘??
def bfs(st):
    q = deque()
    global cnt
    q.append(st)
    trace = deque()
    vis[st] = 1
    while q:
        x = q.popleft()
        trace.append(x)
        cnt += 1
        for i in arr2[x]:
            if vis[i] == 1:
                return trace
            if vis[i] == 0:
                q.append(i)
                vis[i] = 1
    return -1
ans = []
for i in range(1,n+1):
    if vis[i] == 0:
        cnt = 0
        s = bfs(i)
        if s == -1:
            continue
        else:
            if cnt > ans_len:
                ans_len = cnt + same
                ans = s
            else:
                continue
#print(same)
# 반례 : 6, [2,3,1,5,4,6]
print(ans_len)
fin = []
for j in ans2:
    fin.append(j)
for i in ans:
    fin.append(i)
fin.sort()
for i in fin:
    print(i)







