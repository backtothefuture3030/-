# 1번문제

result=[88,30,61,55,95]
for i in result:
	if i>=60:
		print("귀하는 %d점으로 합격하셨습니다"%i)
	else :
		print("귀하는 %d점으로 불합격하셨습니다"%i)
#답안

result = [88,30,61,55,95]
for i in range(0,5):
	if result[i]>=60:
		ispass = "합격"
	else:
		ispass = "불합격"
	print("%d번 학생은 %d점으로 %s입니다" %(i+1,result[i],ispass))
# 번호까지 추가하라고 했으면 어려웠을문제.. 리스트 인덱스 활용하자

# 2번문제 너무 답이 길어 주석처리(너무쉬움)
'''for i in range(1,101):
	print (i)
'''
# 3번문제
'''for i in range(1,101):
	if not i%2:
		print(i)
''' # 너무 쉽고 답이 길어서 주석처리

# 4번문제
'''for i in range(1,101):
	if i%2:
		print(i)
''' # 너무 쉽고 답이 길어 주석처리

# 5번문제 

result = 0
for i in range(1,101):
	if i%3==0:
		result+=i
print(result)

# 한동안 나에게 어려웠던 문제. 3의배수의 합을 구하는식. 



#6  투박하게 풀었다. 더깔끔하게 한번더 풀어보자 if문을 사용하지 않은채로.

student = ['A','A','A','O','B','B','O','AB','AB','O']
a=0 
b=0 
o=0 
ab=0
for i in student:
	if i=='A':
		a+=1
	elif i=='B':
		b+=1
	elif i=='O':
		o+=1
	else:
		ab+=1
print("A형은 %d명입니다,B형은 %d명입니다,O형은 %d명입니다,AB형은 %d명입니다" %(a,b,o,ab))




# 7 다시풀어라
result= [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]  # 답은 맞으나, 문제의 조건에 부합하지못함.
i=0
for a in result:
	if a>=80:
		i+=a
print(i)



'''
8 문제 이와같이 나오게 코딩하세요 while 문 이용
*******
 *****
  ***
   *
'''

	








'''
9번문제 이와 같이 나오게 while 문 이용 
*****
****
***
**
*
'''

i=5
while i:
	print("*"*i)
	i-=1

#1번문제 번호까지 추가하여 풀어보세요



