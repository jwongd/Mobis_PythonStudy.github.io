i = 0
while(True):
    i += 1
    a = int(input())
    if a == 0 :
        break
    n1 = a*3
    if n1%2 == 0:
        p = "even"
        n2 = n1/2
    else:
        p = "odd"
        n2 = (n1+1)/2
    n3 = 3*n2
    n4 = int(n3/9)
    print(f"{i}. {p} {n4}")
