from itertools import combinations

a = input("입력 : ") 
a = list(a)
b = int(input("제외할 숫자 입력 : "))
c = list(combinations(a,len(a)-b))
count=0
t = 0 
for i in c:
    count=0
    for j in range(len(i)//2):
        if i[j]!=i[-j-1]:
            pass
        else:
            count+=1
    if count==(len(i)//2):
        print("Yes")
        t+=1
        break
if t<1:
    print("No")




