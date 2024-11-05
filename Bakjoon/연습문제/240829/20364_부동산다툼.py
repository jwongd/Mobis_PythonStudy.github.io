import sys
input = sys.stdin.readline
import math
n, q = map(int, input().split())
vis = [0] * (n + 1)
for i in range(q):
    a = int(input())
    # 경로 체크를 위한 리스트 생성
    path = []
    cnt = a
    while cnt >= 1:  # 루트까지의 경로를 모두 저장
        path.append(cnt)
        cnt //= 2
    # 경로 역순으로 확인 (루트부터 목적지까지)
    blocked = False
    for pos in path[::-1]:
        if vis[pos] == 1:  # 이미 점유된 땅을 만났다면
            print(pos)
            blocked = True
            break
    if not blocked:  # 경로가 막히지 않았다면
        print(0)
        vis[a] = 1  # 현재 땅을 점유 표시