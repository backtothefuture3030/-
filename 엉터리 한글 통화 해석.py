num = {"영":0,"일":1, "이":2, "삼":3, "사":4, "오":5, "육":6, "칠":7, "팔":8, "구":9, "십":10, "백":100, "천":1000, "만":10000, "억":100000000, "조":1000000000000, "경": 10000000000000000 }
#and i==0
a = "사천구십칠조이천만삼백십육"
won = []
total = 1
for i in range(len(a)):
    if a[0]=='억' or a[0]=='조' or a[0]=='경':
        won.append(-1)
        break
    elif len(a)==4 and a[1]=='억' and a[3]=='천':
        total = (num[a[0]]*num['억'])+(num[a[2]]*num['천']*10000)
        won.append(total)
        break
    elif len(a)==1:
        won.append(num[a[i]])
    elif (total==1 and i==0) :
        total=1
        total*=num[a[i]]
    elif a[i]=='만' or a[i]=='천' or a[i]=='백' or a[i]=='십' or a[i]=='억' or a[i]=='조' or a[i]=='경' :
        total*=num[a[i]]
        if i<len(a)-1:
            if  a[i+1]=='만' or a[i+1]=='천' or a[i+1]=='백' or a[i+1]=='십' or a[i+1]=='억' or a[i+1]=='조' or a[i+1]=='경' :
                pass
            else:
                won.append(total)
        else:
            won.append(total)
    else:
        total=1
        total*=num[a[i]]
        if i==len(a)-1:
            won.append(total)
if -1 in won:
    print("False")
else:
    print(won)
    print(sum(won))



