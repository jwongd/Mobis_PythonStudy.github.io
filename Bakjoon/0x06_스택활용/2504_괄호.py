def right(x):
    x = list(x)
    st = []
    for i in x:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')':
            if st and st[-1] == '(':
                st.pop()
            else: # '[])'
                st.append(i)
        else:
            if st and st[-1] == '[':
                st.pop()
            else:
                st.append(i)
    if len(st) == 0:
        return True
    else:
        return False
n = input()
if right(n) == 0:
    print(0)
    exit(0)




