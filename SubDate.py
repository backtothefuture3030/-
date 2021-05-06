
S="20070301"
Y = int(S[:4])
M = int(S[4:6])
D = int(S[6:])

total=0
year = (Y-1)*365 + (Y-1)//4 - (Y-1)//100 + (Y-1)//400

total+=year
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0 and year%100!=0 or year%400==0:
    mon[1]=29
else:
    mon[1]=28

i=1
while i < M:
    total+=mon[i]
    i+=1

total+=D

print(total)


def SubDate(s1 , s2):
    q=[]
    for i in [s1,s2]:
        Y=int(i[:4])
        M=int(i[4:6])
        D=int(i[6:])
        total=0
        year = (Y-1)*365 + (Y-1)//4 - (Y-1)//100 + (Y-1)//400
        total+=year
        mon = [31,28,31,30,31,30,31,31,30,31,30,31]
        if Y%4 ==0 and Y%100!=0 or Y%400==0:
            mon[1]=29
        else:
            mon[1]=28
        i=1
        while i<M:
            total+=mon[i]
            i+=1
        total+=D
        q.append(total)
    if len(q)==2:
        print(abs(q[0]-q[1]))

SubDate("20200101","20210311")


    




