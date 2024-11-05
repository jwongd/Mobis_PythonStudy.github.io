a,b = map(int,input().split())
cnt = 0
c = 0
if a==b:
    cnt = 0
    print(cnt+1)
    exit(0)
while(b>a):
    cnt+=1
    if b%2 == 0:
        b = b//2
    elif b%10 ==1:
        b = b//10
    else:
        break
if a==b:
    print(cnt+1)
else:
    print(-1)