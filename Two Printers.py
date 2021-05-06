
def Printer():
    test = int(input("테스트 개수 : "))
    i=0
    w=[]
    while i<test:
        a=int(input("속도 : "))
        b=int(input("속도 : "))
        c=int(input("페이지 수 : "))
        count=0
        total=0
        while True:
            if total>=c:
                w.append(count)
                break
            count+=1
            if count%a==0 and count%b==0:
                total+=2
            elif count%a==0:
                total+=1
            elif count%b==0:
                total+=1
        i+=1
    for i in w:
        print(i, end=' ')
Printer()
