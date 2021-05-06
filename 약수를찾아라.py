
a = int(input("약수를 알아낼 숫자를 입력하세요 : "))
b=[]
c=[]

for i in range(1,int(a**(1/2))+1):
        if a%i==0:
            b.append(i)
            if i != a//i:
                c.append(a//i)
                
print(b+c[::-1])
print("약수의 개수는 {}개 입니다".format(len(b)+len(c)))



