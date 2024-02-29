t = int(input())
for _ in range(t):
    s = list(input())
    cur = 0
    q1 = [] #커서 왼쪽
    q2 = [] #커서 오른쪽
    for i in s:
        if i == '-':
            if not q1:
                continue
            q1.pop()

        elif i == '<':
            if not q1:
                continue
            q2.append(q1.pop())
            cur -= 1
        elif i == '>':
            if not q2:
                continue
            q1.append(q2.pop())
            cur += 1

        else:
            q1.append(i)
    q1.extend(reversed(q2))
    print(''.join(q1))

