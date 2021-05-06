
#a = [1,6,10,4,7,9,5]


def order():
    a=list(map(int, input("정수 배열을 입력하세요 : ").split()))
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
    return a 

def Subset():
    n = []
    a = order()  
    w=0
    q = {}
    for i in range(1,len(a)):
        if a[i]-1 != a[i-1]:
            n.append(a[w:i])
            w=i
    n.append(a[w:])

    for i in n:
        q[len(i)]=i
    print(max(q),q[max(q)])
Subset()

