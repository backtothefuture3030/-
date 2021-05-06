''' for문

for문의 기본구조

for 변수 in 리스트(튜플, 문자열):
	<실행할 문장1>
	<실행할 문장2>
	...
'''

list1 = ['a','b','c']

for i in list1:
	print(i)

점수 = [90,50,60,45,80] #1번부터 5번까지 학생의 시험점수
학번 = 0

for i in 점수:
	학번 = 학번+1
	if i >=60: print("%d번 학생의 점수는 %d점으로 합격되었습니다..!" %(학번,i))
	else:print("%d번 학생은 %d점으로 불합격되었습니다...!" %(학번,i))

#continue 
학번 = 0 #학번값을 0으로 초기화한다. 윗문에서 반복되므로.
for i in 점수:
	학번= 학번+1
	if i<60: continue
	print("%d번 학생 %d점으로 합격입니다!" %(학번,i))

aa = [('a','b'),('c','d'),('e','f')]
for (i,j) in aa:
	print(i+j)



'''연습문제 풀이

양,음,0 판단문제

k=9
if k>0 :
	print("양수입니다")
elif k<0:
	print("음수입니다")
else:
	print("0입니다")

*******무늬만들기 문제
i=8
while i>0:
	i=i-1
	print(i*'*')

'''
''' for문과 range함수
-range 함수는 두개, 세개의 숫자를 이용하는 함수이다.
 숫자가 두개인 경우 1씩 증가하는 숫자의 리스트를 반환한다.
 숫자가 세개인 경우 마지막 세번 째 숫자는 증가치를 의미한다.

 사용예> range(1,5) ---> 리스트[1,2,3,4] 반환한다. #1부터 1씩 증가하는 5미만숫자 리스트 표현
       range(1,5,2) -> 리스트[1,3] 2씩 증가시킨다.
	   ** (주의) 두번째 숫자는 이하가 아니라 미만까지만 반환을 한다.
'''

for i in range(1,5):
	print(i)
else:   #반복문에서 else절은 루프를 다돌고 난뒤에 항상 수행한다. break문을 사용했을 경우에는 수행되지않는다. 
	print("반복문 종료")
	
''' c언어에 for문과 파이썬의 for문은 근본적으로 다르다.
    파이썬의 for문은 C# foreach루프 비슷하고, java의 for(int i :IntArray) 비슷하다.
	c언어에서 for(int i =0; i<5: i++)과  같이 파이썬에서 표현한다면
	for i in range(0,5)와 같이 표기할 수 있다.
range 함수를 이용해서 구구단 출력하기
'''

for i in range(2,10):
	for j in range(1,10):          
		print("%d*%d=%d" %(i,j,i*j), end=" ")  #for문 안의 for문 i안에 j식  end는 띄어쓰기
	print("") #줄바꾸기위한 명령

# 리스트안에 for문을 이용하여 프로그램 해보기

aa= [1,2,3,4,5,6,7,8,9]

구구단_2 = []

for i in aa:
	구구단_2.append(i*2)  #append 라는건 구구단안 빈리스트에 추가해라는거
print(구구단_2)

구구단_2 = [i*2 for i in aa]
print(구구단_2)

# 5단의 결과값 중에서 짝수만 리스트에 추가하는 예
구구단_5 = [i*5 for i in aa if i%2 ==0]
print(구구단_5)

''' 리스트 내포(List comprehension)의 일반적인 기본적인 구조

 1. [표현식 for 항목 in 반복가능한 객체 if조건]
	  위에서 if조건은 생략이 가능하다.
 2. [표현식 for 항목1 in 반복가능한 객체1 if 조건1
          for 항목2 in 반복가능한 객체2 if 조건2
          .....
		  for 항목 n in 반복가능한객체n if 조건 n] 
'''
#구구단의 결과를 저장하는 리스트 구현
gugudan =[i*j for i in range(2,10)
	for j in range(1,10)]
print(gugudan)

gugudan =[i*j for i in range(2,10)
	for j in range(1,10) ]
