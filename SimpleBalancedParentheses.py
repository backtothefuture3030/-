# 여는괄호 '('와 닫는괄호 ')' 가 짝맞춰서 있어야 성립을 한다.
# 정상적인 괄호면 무조건 짝수개가 나오므로 길의에 반을 나눠 대칭인지 확인한다.

 #input("괄호 사용이 올바른지 확인할 괄호를 입력하세요")
   
#(()()
#()())


#  (()()()())
'''
b = list(a)

count=0

if b[1:len(a)//2]==b[(len(a)//2):len(a)-1] and b[0]=='(' and b[-1]==')':
    print("True")
elif b[0]=='(' and b[-1]==')':
    for i in range(1,len(a)//2):
        if a[i]==a[-i-1]:
            count+=1
print(count)
if count==len(a)//2-1:
    print("true")
else:
    print("False")

'''
# '('로 시작했을때, ')' 이온다면 '('와야함
# '('로 시작했을떄, '(' 이 온다면 '(' ')' 둘다 올수가있다
# ')'로는 시작할 수가없다.
#   전의 문자와 비교를하자
# '(' 와 '(' 이 순서대로 나온다면 길이는 4, ')'는 두개 나와야한다.

 # ()))  2개 '('  (()()(() 2개 '(' ()()()
# 카운트 만큼 ')'가 있어야한다.
a = "(((()))((((((((())))))))))" 
b = list(a)
q=0
cnt =1
if len(a)/2 == b.count(')') and a[0] != a[-1]:
    for i in range(1,len(a)-2):
        if b[i]!=b[-i-1] and b[1]=='(':
            #print("true")
            break
        elif b[i]!=b[i+1]:
            cnt-=1
        elif b[i]==b[i+1]:
            cnt+=1
            q+=i
    if abs(cnt)%2==1 or q==0 or cnt==0:
        print("True")
    else:
        print("false")
else:
    print("False")

