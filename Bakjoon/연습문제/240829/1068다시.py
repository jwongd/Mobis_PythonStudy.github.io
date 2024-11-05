import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
child = [[] for _ in range(n)] # 직속만 취급
delnode = int(input())
for idx,val in enumerate(arr):
    if val == -1: continue
    child[val].append(idx)
#print(*child)
d = []
def dfs(node):
    vis = [0] * (n+1)
    d.append(node)
    vis[node] = 1
    for i in child[node]:
        #print("i:",i)
        if vis[i] == 0:
            vis[i] = 1
            dfs(i)
pp = (arr[delnode])
for i in child[pp]:
    if i == delnode:
        child[pp].remove(i)
dfs(delnode)
cnt = 0
for i in d:
    child[i] = -2
#print(*child)
for i in child:
    if i == []:
        cnt+=1
print(cnt)

'''
9
-1 0 0 5 2 4 4 6 6
4

위와 같은 경우에 루트 노드에 연결된 1 and 2 가 리프 노드가 돼서 2를 출력해야 하는데
 1을 출력하는 것을 발견했다.
 
 def dfs(y):
    global re
    for i in g[y]:
        if not vist[i] and i !=en:
            vist[i]=True
            if g[i]==[]:
                re+=1
            dfs(i)
        elif i==en and len(g[y])==1:#삭제된 노드때문에 리프노드가 된 경우!
            re+=1


n= int(input())
g = [[] for _ in range(n)]
s = list(map(int,input().split()))
for i in range(n):
    if s[i]!=-1:
        g[s[i]].append(i)
    else:
        t = i
en = int(input())
re = 0
g[en]=[]
vist = [False]*(n+1)
vist[t]=True
dfs(t)
print(re)
#트리 노드가 리프 노드인 경우를 더이상 예외처리 안 해도 됨
'''