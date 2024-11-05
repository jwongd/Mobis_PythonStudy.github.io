from itertools import product as pm
from collections import deque
arr= list(map(int,input().split()))
a = [1,2,3,4,5,6,7,8,9]
# d = defaultdict(set) ; d2 =defaultdict(set)
s = set()
l = list(pm(a,repeat =4))
idx = 1
for i in l:
    #print(i)
    i = sorted(i)
    a = ''.join(map(str,i))
    a = int(a)
    s.add(a)
arr = sorted(arr)
def min_clock_number(digits):
    # 가능한 시계 방향 조합을 계산합니다.
    rotated_numbers = [
        int(''.join(map(str, digits))),
        int(''.join(map(str, digits[1:] + digits[:1]))),
        int(''.join(map(str, digits[2:] + digits[:2]))),
        int(''.join(map(str, digits[3:] + digits[:3])))
    ]
    return min(rotated_numbers)
s = sorted(s)
##print("x:",x)
x = min_clock_number(arr)
print(s.index(x)+1)
#print("---")
#print(*s)