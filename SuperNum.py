


def Super(a):
    for i in range(1,a+1):
        b=[]
        for j in range(1,i+1):
            if i%j==0:
                b.append(j)
        try:
            if (i-1)%(sum(b)-i-1)==0:
                print("({},{})".format(i,int((i-1)/(sum(b)-i-1))))
        except Exception:
            pass
        else:
            pass

Super(1000)