def solution(sizes):
    for i in sizes:
        x,y = i[0],i[1]
        if y>=x:
            i[0],i[1] = y,x
    a = 0
    b = 0
    for i in sizes:
        a = max(a,i[0])
        b = max(b,i[1])
    answer = a*b
    return answer