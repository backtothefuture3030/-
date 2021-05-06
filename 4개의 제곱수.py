import random, math


def root(num):
    a= [0,0,0,0]
    while a[0]**2 + a[1]**2 + a[2]**2 +a[3]**2 != num:
        a[0] = int(random.randint(0,int(math.sqrt(num))))
        a[1] = int(random.randint(0,int(math.sqrt(num))))
        a[2] = int(random.randint(0,int(math.sqrt(num))))
        a[3] = int(random.randint(0,int(math.sqrt(num))))
        
    print(a)

root(1572)




