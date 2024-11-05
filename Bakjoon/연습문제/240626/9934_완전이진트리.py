from collections import defaultdict
k = int(input())
num = list(map(int,input().split()))
a = defaultdict(list)
def dfs(arr,depth):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        a[depth].append(arr[0])
        return
    center = (len(arr))//2
    left_arr = arr[:center]
    right_arr = arr[center+1:]
    dfs([arr[center]],depth)
    dfs(left_arr,depth+1)
    dfs(right_arr,depth+1)
dfs(num,0)
for i in a.values():
    print(*i)
#print(a)

