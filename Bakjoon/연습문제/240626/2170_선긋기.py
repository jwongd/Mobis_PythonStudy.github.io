n = int(input())
arr =[]
st_arr = []
en_arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
arr.sort(key= lambda  x: x[0])
for x,y in arr:
    st_arr.append(x)
    en_arr.append(y)
st = st_arr[0]
en = en_arr[0]
ans = 0
for i in range(n):
    #print("st:",st,"en:",en,"st_arr",st_arr[i],"en_arr",en_arr[i])
    if st_arr[i] > en:
        ans += (en-st)
        st = st_arr[i]
        en = en_arr[i]
    else:
        en = max(en_arr[i],en)
ans += (en-st)
print(ans)
