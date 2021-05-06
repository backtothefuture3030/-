import numpy as np 

#a=np.array(range(64)).reshape((8,8))

#print(a)


 # 
def Queens():
    a = np.zeros((8,8))
    r=0
    count=0
    total=0
    while r<8:
        i=int(input("행을 입력하세요"))-1
        j=int(input("열을 입력하세요"))-1
        if i==0 and j==0:   # 아래 네개는 똑같은 젤 꼭짓점 자리
            a[0,0]+=1         # [0,0] [0,1] [1,0] [1,1]
            a[0,1]+=1
            a[1,0]+=1
            a[1,1]+=1
        elif i==0 and j==7:   # [0,7] [0,6] [1,6] [1,7]
            a[0,7]+=1
            a[0,6]+=1
            a[1,6]+=1
            a[1,7]+=1
        elif i==7 and j==0:   # [7,0] [7,1] [6,0] [6,1]
            a[7,0]+=1
            a[7,1]+=1
            a[6,0]+=1
            a[6,1]+=1
        elif i==7 and j==7:   # [7,7] [6,6] [6,7] [7,6]
            a[7,7]+=1
            a[6,6]+=1
            a[6,7]+=1
            a[7,6]+=1
        elif i==0 :   # 아래줄 ,혹은 옆줄 6칸만 먹는
            a[i,j]+=1
            a[i,j-1]+=1
            a[i,j+1]+=1
            a[i+1,j-1]+=1
            a[i+1,j]+=1
            a[i+1,j+1]+=1
        elif i==7:
            a[i,j]+=1
            a[i,j-1]+=1
            a[i,j+1]+=1
            a[i-1,j]+=1
            a[i-1,j-1]+=1
            a[i-1,j+1]+=1
        elif j==0 :
            a[i,j]+=1
            a[i-1,j]+=1
            a[i+1,j]+=1
            a[i,j+1]+=1
            a[i-1,j+1]+=1
            a[i+1,j+1]+=1
        elif j==7:
            a[i,j]+=1
            a[i-1,j]+=1
            a[i+1,j]+=1
            a[i,j-1]+=1
            a[i-1,j-1]+=1
            a[i+1,j-1]+=1
        else:
            for q in [i-1,i,i+1]:
                for w in [j-1,j,j+1]:
                    a[q,w]+=1
        print(a)
        r+=1

    for i in range(8):
        for j in range(8):
            if 0<=a[i,j]<=1:
                count+=1
    if count==64:
        total+=1

Queens()