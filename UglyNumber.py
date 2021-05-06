def ugly(n):
    result = [1]
    while True:
        last = result[-1]
        if len(result)==n:
            return last
        tem = []
        for r in result:
            for t in r*2,r*3,r*5:
                if t > last: 
                    tem.append(t)   # tem(2,3,5)

        result.append(min(tem))


print(ugly(1500))