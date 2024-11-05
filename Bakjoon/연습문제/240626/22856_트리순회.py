from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
tree = defaultdict(list) ; arr = []
for _ in range(n):
    a,b,c = map(int,input().split())
    tree[a] = [b,c]
ans = 0
cnt = 0 ; final_node = 0;cnt2=0
# def final(t):
#     global final_node
#     if tree[t][0] != -1:
#         final(tree[t][0])
#     final_node = t
#     if tree[t][1] != -1:
#         final(tree[t][1])
def inorder(n):
    #vis.add(n)
    global cnt,cnt2
    left,right = tree[n]
    if left != -1 :#and left not in vis:
        cnt += 1
        inorder(left)
    if right != -1 :#and right not in vis:
        cnt += 1
        # cnt2+=1
        inorder(right)
#
def inorder2(n):
   #vis.add(n)
    global cnt2
    left,right = tree[n]
    if right != -1:# and right not in vis:
        inorder2(right)
        cnt2 += 1

#vis = set()
inorder(1)
#vis = set()
inorder2(1)
print(cnt)
print(cnt2)
ans = cnt*2 - cnt2
print(ans)