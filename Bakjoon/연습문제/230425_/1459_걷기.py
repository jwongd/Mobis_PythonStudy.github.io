x1,y1,w,s = map(int,input().split()) #s : 대각선
if 2*w > s:
    a = min(x1,y1)
    ans = a*s
    #나머지 더하기
    b = abs(x1-y1)
    if w>s:
        if b % 2 == 0:
            ans+=b*s # 2n칸시, /\ 이렇게 대각 2번으로 갈수있음
        else:
            ans+= (b-1)*s+w
    else: #애초에 대각선이 더 오래걸릴 때
        ans += b*w
else: #2*w <= s
    ans = (x1+y1)*w
print(ans)