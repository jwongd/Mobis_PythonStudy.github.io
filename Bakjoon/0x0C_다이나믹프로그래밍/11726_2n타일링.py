N = int(input())
list = [0]*1001
list[1] = 1
list[2] = 2
for i in range(3,N+1):
    list[i] = list[i-1] + list[i-2]
print(list[N]%10007)
