def solution(t, p):
    answer = 0
    lenp = len(p)
    lent = len(t)
    for i in range(lent-lenp+1):
        if int(t[i:i+lenp]) <= int(p):
            answer += 1

    return answer