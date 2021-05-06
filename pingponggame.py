def pingpong(a):
    count=0
    b=0
    i=0
    c=[]
    while i<=a:
        while True:
            i+=1
            count+=1
            b+=1
            c.append(b)
            if count%7==0 or '7' in str(count) :
                break
        while True:
            i+=1
            count+=1
            b-=1
            c.append(b)
            if count%7==0 or '7' in str(count) :
                break
    print(c[a-1])

pingpong(100)
        




