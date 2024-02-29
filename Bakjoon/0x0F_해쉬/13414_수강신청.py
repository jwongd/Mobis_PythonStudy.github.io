a,b = map(int,input().split())
d = {}
d2 = {}
for i in range(b):
    num = int(input())
    if num in d2:
        c = d2[num] #중복된 num의 index
        del d[c]
        del d2[num]
        d[i] = num
        d2[num] = i
    else:
        d[i] = num
        d2[num] = i
for i in range(a):
    print(d[i])