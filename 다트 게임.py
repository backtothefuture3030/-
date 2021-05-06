

def Dart(): 
    a=input("다트결과 입력 : ")
    a=list(a)   
    for j in range(len(a)):
        if a[j]=='S' or a[j]=='D' or a[j]=='T' or a[j]=='#' or a[j]=='*':
            pass
        elif a[j]=='1' and a[j+1]=='0':
            a[j]='10'
            a[j+1]='1'
    dic = {'S':1, 'D':2, 'T':3, '#':-1,'*':2}
    total = 1
    n=[]
    p=[]
    for i in range(len(a)):
        if a[i]=='S' or a[i]=='D' or a[i]=='T':
            total**=dic[a[i]]
            if i<=len(a)-2 and a[i+1]=='#' :
                total*=-1
                n.append(total)
                total=1
            else:
                n.append(total)
                total=1
        elif a[i]=='#':
            pass
        elif a[i]!='*':           # 문자열로 된 숫자면 가능
            total*=int(a[i])
        elif a[i]=="*":
            t = a.index(a[i])
            a[i]=1
            p.append(t)
    if len(p)==3:
        n[0]*=4
        n[1]*=4
        n[2]*=2
    elif len(p)==2:
        if p[0]==2 and p[1]==5:
            n[0]*=4
            n[1]*=2
        elif p[0]==2 and p[1]==7:
            n[0]*=2
            n[1]*=2
            n[2]*=2
        elif p[0]==4 and p[1]==7:
            n[0]*=2
            n[1]*=4
            n[2]*=2
    elif len(p)==1:
        if p[0]==2:
            n[0]*=2
        elif p[0]==4 or p[0]==5:
            n[0]*=2
            n[1]*=2
        elif p[0]==6 or p[0]==7:
            n[1]*=2
            n[2]*=2
    print(sum(n))

Dart()





