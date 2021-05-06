import timeit
import psutil

p = psutil.Process()
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
l = list(map(int,input('배열을 입력하세요 : ').split()))
start_time = timeit.default_timer() 
r = []
if a==len(l):
    i=0
    c=[]
    while i<=a-b:
        for w in range(b):
            c.append(l[i+w])
        r.append(max(c))
        i+=1
terminate_time = timeit.default_timer()
print("%f초 걸렸습니다." % (terminate_time - start_time)) 
print(p.memory_info())
print(r)
    






