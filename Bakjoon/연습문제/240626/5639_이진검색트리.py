import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)
arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
def bfs(arr):
    if len(arr) == 0: return
    if len(arr) == 1:
        print(arr[0])
        return
    root = arr[0]
    index = len(arr)
    for i in range(1,len(arr)):
        if arr[i] > root:
            index = i
            break
    left_arr = arr[1:index]
    right_arr = arr[index:]
    bfs(left_arr)
    bfs(right_arr)
    print(root)
bfs(arr)
