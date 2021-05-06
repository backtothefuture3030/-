'''
n = int(input("다리를 건너는 트럭의 수 : "))
w = int(input("다리의 길이 : "))
l = int(input("다리의 최대하중 : "))
a = [] # 트럭 무게들
total=0  # 트럭 무게 총합
q=0 
count=0  # 같이 지나가는 트럭개수
time = 0 # 지나는 시간
while q<n:
    a.append(int(input("트럭의 무게 : ")))  # a = [7,4,5,6]
    q+=1
for i in a:
    total+=i
    if total<=l:
        time+=w
    else:
        time+=1
        total=i

if total<l and len(a)>1:
    time+=w


print(time)

'''

def cross(W, L, trucks):
    bridge = [0] * W
    time = 0
    while bridge:
        time += 1
        print(bridge)
        bridge.pop(0)
        print(bridge)
        if trucks:
           if sum(bridge) + trucks[0] <= L:
               bridge.append(trucks.pop(0))
           else:
               bridge.append(0)

        #print(bridge); input()

    return time
print(cross(2,10,[7,4,5,6]))
