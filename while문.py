'''while문
** while문의 구조

while<조건문>:
	<실행할 명령문1>
	<실행할 명령문2>
	<실행할 명령문3>
	....
'''

aa = 0
while aa<10:
	aa = aa+1
	print("aa 값은 %d 입니다" %aa)
	if aa==10:
		print("종료합니다")

'''무한루프 예

while 1:
	<실행할 명령문1>
	<실행할 명령문2>
	....

while 1:
	print("무한반복 됩니다")
'''

#보조제어문(break, continue)
m=100
n=10 
while m:      # while 뒤에 m, 즉 0이 아닌숫자가 올때 참임을 의미 그래서 계속반복됨                  
	n=n-1
	print("현재 %d 입니다" %n)

	if not n:               # not뒤 9,8,7,6,5..에서 앞에 not 이붙으므로 숫자앞 not은 not+true는 거짓. 그래서 위로 돌아가는것.
		print("n의 값이 0입니다")
		break  #while문을 빠져나간다. (break)

#1에서 부터 10까지의 정수중 홀수를 출력하는 코드
i = 0
while i<10:
	i=i+1
	if i % 2 ==0: continue #continue문은 while문의 맨처음(i<10)으로 돌아가게 하는 명령문
	print(i)

