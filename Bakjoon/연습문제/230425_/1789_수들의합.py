s = int(input())
i = 1
sum = 0
while(True):
    sum += i
    if sum>s:
        break
    i += 1
print(i-1)
