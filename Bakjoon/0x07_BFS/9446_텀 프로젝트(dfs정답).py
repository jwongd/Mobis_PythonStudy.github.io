import sys
sys.setrecursionlimit(10 ** 6)

T = int(input())
for _ in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    student.insert(0, 0)  # 인덱스 편의를 위해서 삽입
    vis = [0] * (N + 1)

    for i in range(1, N + 1):
        if vis[i] == 0:  # 아직 팀이 없는 경우
            student_number = i
            # 팀 구성한다고 가정
            while vis[i] == 0:
                vis[i] = student_number
                i = student[i]
            # 역순으로 순환하면서 사이클 확인
            while vis[i] == student_number:
                vis[i] = -1
                i = student[i]
    result = N - vis.count(-1)
    print(result)