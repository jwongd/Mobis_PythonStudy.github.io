import math
n = (input())
num = "0123456789"
arr = [0]*10
for i in n:
    for j in range(len(num)):
        if i == num[j]:
            arr[j] += 1
x = arr[6]
y = arr[9]
arr[6]= math.ceil((x+y)/2)
arr[9]= arr[6]
print(max(arr))




