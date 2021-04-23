"""
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다."""

T = int(input())
while T>0:
    T-=1
    a= {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14}
    b = {1:1,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
    k=int(input())
    n=int(input())
    count=0
    total=0
    while k>0:
        k-=1
        count+=1
        total+=1
        if count%2==1:
            if total>2:
                for i in range(2,len(b)+1):
                    b[i]=0
                for i in range(2,len(a)+1):
                    for j in range(1,i+1):
                        b[i]+=a[j]
            else:
                for i in range(2,len(a)+1):
                    for j in range(1,i+1):
                        b[i]+=a[j]
        else:
            for i in range(2,len(a)+1):
                a[i]=0
            for i in range(2,len(b)+1):
                for j in range(1,i+1):
                    a[i]+=b[j]
    if count%2==1:
        print(b[n])
    else:
        print(a[n])





