import sys
from collections import defaultdict, Counter
input = sys.stdin.readline
n,m = map(int,input().split())
d = defaultdict(str)
l = []
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        #d[word] += 1
        l.append(word)
l_cnt = Counter(l)
l_sort = sorted(l_cnt.items() , key = lambda x: (-x[1],-len(x[0]),x[0]))
for i,j in l_sort:
    print(i)