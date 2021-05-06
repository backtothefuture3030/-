total=0
for i in range(100,1000):
    count=0
    a=i*int(str(i)[::-1])
    for j in range(len(str(a))-1):
        if int(str(a)[j])<=int(str(a)[j+1]):
            count+=1
    if count==len(str(a))-1:
        total+=1


print(total)