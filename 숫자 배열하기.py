import random

a = [1,2,3,4,5,6,7,8,9]
n=0

while n<5:
    n+=1
    random.shuffle(a)
    for i in a:
        print(i, end=' ')
    print()





        

