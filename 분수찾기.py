
'''
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.'''

a=int(input())
first = 1
plus=2
count=1
bunmo = 1
pandan=0  # 홀짝번쨰 판단
while True:
    if a==1:
        print("1/1")
        break
    count+=1
    first+=plus
    pandan+=1
    if a<=first:
        if pandan%2==0:
            count-=(first-a)
            bunmo+=(first-a)
            print("{}/{}".format(bunmo,count))
        else:
            count-=(first-a)
            bunmo+=(first-a)
            print("{}/{}".format(count,bunmo))
        break
    plus+=1

