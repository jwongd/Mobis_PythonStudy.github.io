T = int(input())
sxx = []
for _ in range(T):
    day = int(input())
    num = list(map(int, input().split()))
    st = []
    ans = 0
    print("=====================")
    for idx,i in enumerate(num):
        while st and st[-1] > i:  # 처음 딱 꺾이는 순간
            x = st.pop()
            print("x:",x)
            while st:
                y = st.pop()
                ans += (x - y)
        if idx == (len(num) - 1):
            while st and st[-1]<= i:
                x2 = st.pop()
                ans += (i - x2)
        else:
            st.append(i)
        print("st:",st)
    sxx.append(ans)
for i in sxx:
    print(i)

