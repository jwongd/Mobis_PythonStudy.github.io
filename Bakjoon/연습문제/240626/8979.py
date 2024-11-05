from bisect import bisect_right, bisect_left
n,k = map(int,input().split())
d = {}
l = {}
sc = []
for _ in range(n):
    idx, a,b,c= map(int,input().split())
    score = int(1e14)*a + int(1e7)*b + c
    l[idx] = score
    sc.append(score)
    #d[idx] =((a,b,c))
# d2 = dict(sorted(d.items(), key = lambda x: (-x[1][0],-x[1][1],-x[1][2])))
# print(d2)
l = dict(sorted(l.items(), key= lambda x: -x[1]))
sc.sort(reverse= True)
# print(l)
# print(sc)
# print(l[k])
a = sc.index(l[k])
print(a+1)