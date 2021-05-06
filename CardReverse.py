
a = list(range(1,21))
count=0
while count<10:
    c=[]
    q = int(input("시작수를 입력하세요"))
    w = int(input("마지막수를 입력하세요"))
    if not 1<=q<=w<=20:
        print("1<=q<=w<=20 형식의 수를 넣으세요")
        break
    count+=1
    for i in a[q-1:w]:
        c.append(i)
    del a[q-1:w]
    for num in c:
        a.insert(q-1,num)
    print(a)

