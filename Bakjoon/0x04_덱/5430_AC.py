from collections import deque
T = int(input())
for i in range(T):
    op = input().strip()
    size = int(input())
    flag = 0
    num = input().strip()
    q = deque(num[1:-1].split(','))
    if size == 0: q = deque()
    R_cnt = 0
    for i in op:
        if i == 'R':
            R_cnt += 1
        else:
            if len(q) == 0:
                print('error')
                flag = 1
                break
            else:
                if R_cnt%2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag == 1:
        continue
    else:
        if R_cnt % 2 == 0:
            print('['+','.join(q)+']')
        else:
            q.reverse()
            print('['+','.join(q)+']')



