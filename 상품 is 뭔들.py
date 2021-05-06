


a=int(input("수입력"))
b=int(input("수입력"))
rate=0
for i in range(a+1,b+1):  # 2 3 4
    count=0
    for j in range(2,i):  # 2 3
        if i%j==0:
            count+=1
    if count%2==1:
        rate+=1
def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

print("{}/{}".format(int(rate/gcd(b-a,rate)),int((b-a)/gcd(b-a,rate))))

