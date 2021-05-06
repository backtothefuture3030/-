
'''
숫자를 받는다
소수점 자리가 있을수있으므로 고려하지않기위해 int로 바꾼다.   원래 -3245.24에서 int(-3245.24)를 뺴서 0.24를 얻은후 ".24"를 "3,245"에 더한다
숫자의 -4 -8 -12 이런식으로 마이너스 4의배수 자리에 ','를 넣는다

'''

a=20000000	   
q=[]
t=1
i=1
if float(a)-int(a)==0:
    w=str(a)
    while i<len(w):
        q.append(w[-i])
        i+=1
    q.append(w[0])

    while 2*t+1<len(w):
        if t%2==1:
            q.insert(2*t+1,',')
            t+=1
        else:
            t+=1

    print(''.join(q)[::-1])

else:
    d = abs(float(a)-int(a))
    e=str(int(a))
    while i<len(e):
        q.append(e[-i])
        i+=1
    q.append(e[0])
    while 2*t+1<len(e):
        if t%2==1:
            q.insert(2*t+1,',')
            t+=1
        else:
            t+=1
    print(''.join(q)[::-1]+str(d)[1:])





def pointer(char):
    temp = ''
    a = char[::-1]
    for i in range(0, len(a), 3):
        temp += a[i:i+3] + ','
    a = temp[::-1]
    if a[0] == ',':
        temp = a[1:]
    return temp
a = str(input('enter the number: '))
if a.find('.') == -1:
    print(pointer(a))
else:
    idx = a.find('.')
    b = a[0:idx]
    print(pointer(b) + a[idx:])

