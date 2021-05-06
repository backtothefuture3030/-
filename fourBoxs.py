from itertools import product
from itertools import combinations

ax1,ay1,ax2,ay2 = map(int,input("좌표 : ").split())
bx1,by1,bx2,by2 = map(int,input("좌표 : ").split())
cx1,cy1,cx2,cy2 = map(int,input("좌표 : ").split())
dx1,dy1,dx2,dy2 = map(int,input("좌표 : ").split())


ax = set(list(range(ax1,ax2+1)))   #각각의 좌표의 최소 최댓값
ay = set(list(range(ay1,ay2+1)))
bx = set(list(range(bx1,bx2+1)))
by = set(list(range(by1,by2+1)))
cx = set(list(range(cx1,cx2+1)))
cy = set(list(range(cy1,cy2+1)))
dx = set(list(range(dx1,dx2+1)))
dy = set(list(range(dy1,dy2+1)))


SA = (max(ax)-min(ax))*(max(ay)-min(ay)) # 각각의 넓이
SB = (max(bx)-min(bx))*(max(by)-min(by))
SC = (max(cx)-min(cx))*(max(cy)-min(cy))
SD = (max(dx)-min(dx))*(max(dy)-min(dy))

total = SA+SB+SC+SD   # 겹쳐지든 상관없이 모든 사각형 넓이를 더한다.

X=[ax,bx,cx,dx]
Y=[ay,by,cy,dy]

G = list((combinations(X,2)))
W = list((combinations(Y,2)))
E = list((combinations(X,3)))  
R = list((combinations(Y,3))) 


for i,q in zip(range(len(G)),range(len(W))):    #0~5까지 총 6회 반복
    try:
        (max(list(G[i])[0]&list(G[i])[1])-min(list(G[i])[0]&list(G[i])[1]))*(max(list(W[i])[0]&list(W[i])[1])-min(list(W[i])[0]&list(W[i])[1]))
    except:
        pass
    else:
        total-=((max(list(G[i])[0]&list(G[i])[1])-min(list(G[i])[0]&list(G[i])[1]))*(max(list(W[i])[0]&list(W[i])[1])-min(list(W[i])[0]&list(W[i])[1])))

for j,k in zip(range(len(E)),range(len(R))):
    try:
        (max(list(E[j])[0]&list(E[j])[1]&list(E[j])[2])-min(list(E[j])[0]&list(E[j])[1]&list(E[j])[2]))*(max(list(R[k])[0]&list(R[k])[1]&list(R[k])[2])-min(list(R[k])[0]&list(R[k])[1]&list(R[k])[2]))
    except:
        pass
    else:
        total+=((max(list(E[j])[0]&list(E[j])[1]&list(E[j])[2])-min(list(E[j])[0]&list(E[j])[1]&list(E[j])[2]))*(max(list(R[k])[0]&list(R[k])[1]&list(R[k])[2])-min(list(R[k])[0]&list(R[k])[1]&list(R[k])[2])))


try:
    (max(ax&bx&cx&dx)-min(ax&bx&cx&dx))*(max(ax&by&cy&dy)-min(ay&by&cy&dy))
except:
    pass
else:
    total-=(max(ax&bx&cx&dx)-min(ax&bx&cx&dx))*(max(ax&by&cy&dy)-min(ay&by&cy&dy))

print(total)



