x = input()
y = input()
z = ''
set_x = set(x)
set_y = set(y)
set_xy = set_x & set_y
for i in set_xy:
    z += i*min((x.count(i)),(y.count(i)))
answer = len(x)+len(y)-(len(z)*2)
print(answer)




