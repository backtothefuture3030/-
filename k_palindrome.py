
'''
k-palindrome 은 문자열에서 최대 k개의 문자를 제거했을 때 palindrome이 되는 문자열을 말한다.

문자열 S와 정수값 K가 주어질 때 주어진 문자열이 k-palindrome일 경우 "YES", 아닐경우에는 "NO"를 출력하시오. (단, S의 최대길이는 20,000, K의 범위는 0<=K<=30)


'''

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





