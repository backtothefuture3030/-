
a=[0,1,1]   # 0 1 1 2 3 5 8 13 21 34 55
n=1000
w=2
total=0

while w<n:
    total+=a[1]
    del a[0]
    total%=4294967291
    a.append(total)
    w+=1
    print(a)
    

print(total)




