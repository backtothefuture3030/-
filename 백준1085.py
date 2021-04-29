x,y,w,h = map(int,input().split())

a = []
a.append(x)
a.append(y)
a.append(abs(w-x))
a.append(abs(h-y))
print(min(a))


'''
if x<w-x:
    if y<h-y:
        if x<y:
            print(x)
        else:
            print(y)
    elif x<h-y:
        print(x)
    elif h-y<x:
        print(h-y)
elif w-x<x:
    if y<h-y:
        if w-x<y:
            print(w-x)
        else:
            print(y)
    elif w-x<h-y:





if w-x>h-y :
    if x<w-x:
        print(x)
    else:
        print(h-y)
else:
    print(w-x)
'''