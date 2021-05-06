

def Josephus(a,b):
    count=0
    c=[]
    for i in a:
        count+=1
        if count%b==0:
            if len(set(c))==len(set(a))-1:
                pass
            else:
                c.append(a[count-1])
        else:
            a.append(a[count-1])
    a_sub_c = [x for x in a if x not in c]
    print("생존자는 : {}번째 사람입니다".format(set(a_sub_c)))


Josephus(list(range(1,(int(input("생존자를 입력하세요 : "))+1))),b=int(input("간격을 입력하세요 : ")))

    

# while문을 사용하면 간단하다
def Josephuss(n,k):
    a = list(range(1,n+1))
    m = k - 1
    b = 0
    while len(a) > 1:
        b = ((len(a)+b)%k)
        del a[m::k]
        m = k - b - 1
    return a

print (Josephuss(10,3))