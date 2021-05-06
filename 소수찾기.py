

total=0
i=int(input())
a = list(map(int,input().split()))

if len(a)==i:
    for q in a:
        count=0
        for w in range(1,q+1):
            if q%w==0:
                count+=1
        if count==2:
            total+=1
    print(total)
else:
    pass