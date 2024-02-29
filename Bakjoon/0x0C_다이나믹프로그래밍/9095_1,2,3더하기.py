N = int(input())
list = [0]*11
for _ in range(N):
    a = int(input())
    list[1] = 1
    list[2] = 2
    list[3] = 4
    for i in range(4,a+1):
        list[i] = list[i-1] + list[i-2] + list[i-3]
    print(list[a])