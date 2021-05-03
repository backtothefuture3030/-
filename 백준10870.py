
def pibonacci(n):
    a=[0,1]
    b=[]
    i=0
    if n==0:
        print(0)
        exit()
    while i<=n-2:
        i+=1
        a.append(sum(a))
        del a[0]
    print(a[1])
pibonacci(int(input()))



'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        '''