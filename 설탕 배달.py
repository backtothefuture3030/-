'''
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면,
더 적은 개수의 봉지를 배달할 수 있다.
'''
n=int(input())
three=0 
five=n//5
n%=5
while five>=0:
    if n%3==0:
        three=n//3
        n%=3 
        break
    five-=1 
    n+=5
print(n==0 and (five+three) or -1)
