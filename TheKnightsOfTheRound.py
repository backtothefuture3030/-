import math
a=float(input("삼각형 한변의 첫번째 길이를 입력하세요 : "))
b=float(input("삼각형 한변의 두번째 길이를 입력하세요 : "))
c=float(input("삼각형 한변의 세번째 길이를 입력하세요 : "))
s=float((a+b+c)/2)

A = (s*(s-a)*(s-b)*(s-c))**(1/2)

r = 2*A/(a+b+c)
print("The radius of the round table is : {}".format(round(r,3)))