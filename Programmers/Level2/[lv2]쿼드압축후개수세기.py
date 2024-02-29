def solution(arr):
    num_0 = 0
    num_1 = 0

    def mak(x, y, l):
        global num_0
        global num_1
        val = arr[x][y]
        l = l // 2
        flag = 0
        for i in range(x, x + l):
            for j in range(y, y + l):
                if val != arr[i][j]:
                    flag = 1
                    mak(x, y, l)
                    mak(x + l, y, l)
                    mak(x, y + l, l)
                    mak(x + l, y + 1, l)
            if flag == 0:
                if val == 0:
                    num_0 += 1
                else:
                    num_1 += 1

    mak(0, 0, len(arr))
    answer = [num_0, num_1]
    return answer