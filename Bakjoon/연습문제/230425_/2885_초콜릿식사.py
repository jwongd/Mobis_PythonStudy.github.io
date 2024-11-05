k = int(input())
arr = [2**i for i in range(20)]
# 적어도 k개 정사각형을 먹어야 함
cut = 0 # 최소 몇번 쪼개야하는지?
if k in arr:
    ans = []
    ans.append(k)
    ans.append(0)
    print(*ans)
else:
    # 6 --> 110(2) 7 --> 111(2) 4 --> 100 2--> 010
    a = bin(k)[2:]
    # print(len(a))
    #print(a)
    b = 1 << (len(a))
    for i in range(len(a)): #0,1,26
        #print(a[i])
        if a[i] == '1':
            #print(i)
            cut = i+1
    ans = []
    ans.append(b)
    ans.append(cut)
    print(*ans)