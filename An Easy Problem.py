
def Problem(a):
    if a==0:
        exit()
    b = str(bin(a)).count('1')
    while True:
        a=a+1
        if str(bin(a)).count('1')==b:
            print(a)
            break
Problem(int(input("숫자 입력 : ")))