h,m,s = map(int,input().split())
time = int(input())
h1 = time//3600
time -= 3600*h1
m1 = time//60
time -= 60*m1
s1 = time
h2 = (h+h1)
m2 = (m+m1)
s2 = (s+s1)
if s2 >= 60:
    s2 = s2%60
    m2 += 1
if m2 >= 60:
    m2 = (m2)%60
    h2 += 1
if h2 >= 24:
    h2 = h2%24
# print(h1,m1,s1)
print(h2,m2,s2)