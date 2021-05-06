x,y,w,h = map(int,input().split())

a = []
a.append(x)
a.append(y)
a.append(abs(w-x))
a.append(abs(h-y))
print(min(a))


