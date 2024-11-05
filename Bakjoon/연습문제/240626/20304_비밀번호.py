#안전거리 : and처리했을 때 1의 개수
#안전도 : 모든 비밀번호와의 안전 거리 중 최소값
n = int(input()) #계정 비밀번호 최대값 (2진수로 몇자리?)
m = int(input()) #로그인 시도에 사용된 비밀번호 개수
password = list(map(int,input().split()))
def bits(x):
    cnt = 0
    while x:
        x &= (x-1)
        cnt+=1
    return cnt
for i in range(n):
    for j in password:
        #i를 비번으로 설정