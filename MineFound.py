
import numpy as np

# 각자리의 순서대로 인근에 붙어있는 자리에 폭탄 개수를 count 함수로 센후 그자리에 
# '.' 대신 숫자를넣는다


b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

def Mine(a):
    q=[]
    for i in range(len(a)):
        if a[i]=="\n":
            pass
        else:
            q.append(a[i])
    
        

Mine("*...\n....\n.*..\n....")    

print("*...\n....\n.*..\n....")