



f = open('E:/Word Counting.txt','r')
line = f.read()
c = list(line.split())
count=0
d=[]
e={}
a={}
w=0
for i in c:                     # ',' , '.' 가지고있는 단어 ',' , '.' 없애기
    if i[-1]==',' or i[-1]=='.':
        i=i[:-1]
        d.append(i)
    else:
        d.append(i)
for i in set(d):              # 집합과 리스트의 반복문으로 중복단어 세기
    count=0
    for j in d:
        if i==j:
            count+=1
    e[i]=count
for key, value in e.items():   # 벨류값이 1인 딕셔너리 삭제
    if value!=1:
        a[key]=value
a = sorted(a.items(),reverse=True,key=lambda item:item[1])
while w<10:
    print(a[w][0],a[w][1])
    w+=1









