import random

loop = int(input("반복횟수를 입력하세요 : "))
count=0
i=0
while i<loop:
    x = random.uniform(0,1.0) 
    y = random.uniform(0,1.0) 
    if x**2+y**2<=1:
        count+=1
    i+=1

print("원주율은 {}".format(count/loop*4))

