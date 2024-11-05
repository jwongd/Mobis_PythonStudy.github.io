import math
a,b,v = map(int,input().split())
ans = (v-b)/(a-b)
print(math.ceil(ans))
math.lc