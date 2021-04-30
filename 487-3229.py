
def jeon(j):
    Alpha = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,
    '-':'-','1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'10':10}
    c=[]
    count=0
    cnt = {}
    for d in j:
        b=''
        for i in d:
            b+=str(Alpha[i])
        if len(b)>8:
            d = b.replace('-','')
            e = d[:3]+'-'+d[3:]
            c.append(e)
        elif len(b)<8:
            d = b[:3]+'-'+b[3:]
            c.append(d)
        else:
            c.append(b)
        count+=1
    for w in c:
        try: cnt[w]+=1
        except: cnt[w]=1
    revers = {}
    for k,v in cnt.items():
        revers[v]=k
    del revers[1]
    cnt = {}
    for k, v in revers.items():
        cnt[v]=k
    print(cnt)

jeon(['4873279',
'ITS-EASY',
'888-4567',
'3-10-10-10',
'888-GLOP',
'TUT-GLOP',
'967-11-11',
'310-GINO',
'F101010',
'888-1200',
'-4-8-7-3-2-7-9-',
'487-3279'])


        
