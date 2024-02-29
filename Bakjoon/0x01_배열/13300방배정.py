import math
from collections import Counter
n,k = map(int,input().split())
l =[]
man = []
wom = []
num ="123456"
stu_man = {}
stu_wom = {}
answer = 0
for _ in range(n):
    x,y = map(int, input().split())
    if x == 1:
        man.append(y)
    else:
        wom.append(y)
stu_man = Counter(man)
stu_wom = Counter(wom)
for _,i in stu_man.items():
    answer+= math.ceil(i/k)
for _,j in stu_wom.items():
    answer+=math.ceil(j/k)
print(answer)