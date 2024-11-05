import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
line = []
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    line.append((a,b))
q = int(input())
def answer(a):
    if len(tree[a]) >= 2:
        return "yes"
    else:
        return "no"
def ans2(a,b):
    return "yes"

for _ in range(q):
    ques , num = map(int,input().split())
    if ques == 1:
        print(answer(num))
    else:
        a,b = line[num-1]
      #  print("a:",a,"b:",b)
       # print(*tree)
        print(ans2(a,b))





