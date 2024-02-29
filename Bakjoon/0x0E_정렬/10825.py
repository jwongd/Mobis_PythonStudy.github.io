n = int(input())
li = []
for i in range(n):
    a,b,c,d = input().split()
    li.append([a,int(b),int(c),int(d)])
li = sorted(li,key = lambda x: [-x[1],x[2],-x[3],x[0]])
for i in li:
    print(i[0])