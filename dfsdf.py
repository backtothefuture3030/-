def secret_map(arr1,arr2):
    q=[]
    w=[]
    z=[]
    t =''
    for i in arr1:
        a = int(bin(i)[2:])  
        q.append(a)
    for j in arr2:
        b = int(bin(j)[2:])
        w.append(b)
    for a in range(len(arr1)):
        z.append(q[a]+w[a])
    for i in z:
        r = str(i)
        print()
        for v in range(len(r)):
            if r[v]=='1' or r[v]=='2':
                t+=
            else:
                t+=
    
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
secret_map(arr1,arr2)
