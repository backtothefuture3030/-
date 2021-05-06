
def hIndex(a):
    b=[]
    count=0
    for i in a:
        if min(a)<=i:
            count+=1
            if min(a)<=count:
                b.append(min(a))
                a.remove(min(a))  
    print(max(b))
a = [0,15,4,0,7,10,0]
hIndex(a)

def gIndex(a):
    b=[]
    count=0
    for i in a:
        if min(a)<=i:
            count+=1
            if sum(a)>=count**2:
                b.append(count)
    print(max(b))

a = [0,15,4,0,7,10,0]
gIndex(a)






    