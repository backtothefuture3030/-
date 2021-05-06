# 3 1 4 1 5 9 2 6

# 1 3 4 1 5 9 2 6    1~3 2 
# 1 3 1 4 5 9 2 6    1~3 2 
# 1 1 3 4 5 9 2 6    1~4 5
# 1 1 3 4 5 2 9 6    1~4  5 
# 1 1 3 4 2 5 9 6    1~4   4
# 1 1 3 2 4 5 9 6    1~3   3
# 1 1 2 3 4 5 9 6    1~5   4 
# 1 1 2 3 4 5 6 9  # swap 8번  1~9 9

# 3 1 4 1 5 9 2 6
# 1 3 4 1 5 9 2 6  0,1 

# 1 3 4 1 5 9 2 6  1,2
# 1 3 1 4 5 9 2 6  2,3

# 1 3 1 4 5 9 2 6  3,4

# 1 3 1 4 5 9 2 6  4,5
# 1 3 1 4 5 2 9 6  5,6
# 1 3 1 4 5 2 6 9  6,7

# 1 3 1 4 5 2 6 9  0,1
# 1 1 3 4 5 2 6 9  1,2

# 1 1 3 4 5 2 6 9  2,3

# 1 1 3 4 5 2 6 9  3,4
# 1 1 3 4 2 5 6 9  4,5

# 1 1 3 4 2 5 6 9  5,6

# 1 1 3 4 2 5 6 9  6,7

# 1 1 3 2 4 5 6 9  3,4
# 1 1 3 2 4 5 6 9 

# 1 1 2 3 4 5 6 9 


'''
swap = 0
loop = 0
a = [3, 1, 4, 1, 5, 9, 2, 6]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[i]<=a[j]:
            swap+=1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        
print(swap)
print(loop)
print(a)
'''
'''
a = [3, 1, 4, 1, 5, 9, 2, 6]
swap = 0
loop = 0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
        swap+=1
print(swap)        
print(a)
'''   

swap = 0
loop = 0
a = [3, 1, 4, 1, 5, 9, 2, 6]
b=sorted(a)
while True:
    if a==b:
        loop+=1
        break
    else:
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                swap+=1
        loop+=1

print(loop)
print(swap)
print(a)

