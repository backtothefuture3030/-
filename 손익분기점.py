#total, cost, price =  map(int, input().split())

'''
count=0
while cost<price:
    count+=1
    if price*count > total+cost*count:
        break
if cost>price:
    count=-1
print(count)
'''
'''
count=0
while cost<price:
    if total+cost*count - price*count <0:
        break
    count+=1
if cost>price:
    count=-1
print(count)
'''

total, cost, price = map(int, input().split())
if cost >= price:
    print(-1)
else:
    print(total//(price - cost) + 1)  