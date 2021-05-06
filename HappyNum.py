
e=int(input("숫자를 입력하세요 : "))
a=0
w=0
a=e
c=[]
while True:
    for j in range(len(str(e))):
        w+=int(str(e)[j])**2
    if 1 in c:
        break
    elif w in c:
        break
    else:
        c.append(w)
    e=0
    e+=w
    w=0
if 1 in c:
    print("{} is a Happy Number".format(a))
    
else:
    print("{} is a Unhappy Number".format(a))
    
    

    

    
   