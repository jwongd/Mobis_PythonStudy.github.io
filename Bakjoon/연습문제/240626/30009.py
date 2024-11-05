n = int(input())
x,y,r = map(int,input().split()) # x-r < <x+r
t = []
for _ in range(n):
    t.append(int(input()))
ans1 = 0 ; ans2 = 0
for i in t:
    if i in [x+r,x-r]:
        ans2+=1
    elif x-r < i < x+r:
        ans1 += 1
f = []
f.append(ans1)
f.append(ans2)
print(*f)