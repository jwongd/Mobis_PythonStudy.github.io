import sys
sys.setrecursionlimit(10**7)
N,r,c = map(int,input().split())
ans = 0
def fin(x,y,n):
    global ans
    if n == 0:
        return ans
    size = 2**(n-1) # 4
    if x < size and y >= size:
        ans += size*size
    if x >= size and y < size: #3 section
        ans += size*size*2
    if x >= size and y >= size:
        ans += size*size*3
    r1 = x % size
    c1 = y % size
    return fin(r1,c1,n-1)

print(fin(r,c,N))

