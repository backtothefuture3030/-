import math
# 0 0 0
# 1 1 1
# 1 0 1 
# 1 0 0 # 0 1 0 1 0 1 

'''
def Light(n):
    a={1:0}
    for i in range(2,n+1):
        a[i]=0
    for i in range(1,n+1):
        if n%i==0:
            a[n]+=1

    if a[n]%2==1:
        print("yes")
    else:
        print("no")
    
Light()
'''


def Light(n):
    LastNumber=0
    for i in range(1,n+1):
        if n%i==0:
            LastNumber+=1
    if LastNumber%2==1:
        print("yes")
    else:
        print('no')
Light(6241)
            

'''
def light_switch(input_num):
    return "yes" if math.sqrt(input_num) % 1 == 0 else "no"


print(light_switch(4294967295))
'''
