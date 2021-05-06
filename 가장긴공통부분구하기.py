

def Same(a,d):
    q=len(d)
    b=len(a) 
    c=[]
    e=[]
    for i in range(b):
        c.append(a[i])    
        c.append(a[i:]) 
        c.append(a[i:b//2])    
        c.append(a[i:-1])
    
    for i in range(q):
        e.append(d[i])
        e.append(d[i:])
        e.append(d[i:q//2])
        e.append(d[i:-1])
    print(len(max(list((set(e) & set(c))))))
    print(max(list((set(e) & set(c)))))


Same("photography","autograph")
