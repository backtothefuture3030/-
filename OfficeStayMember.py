# 출근, 퇴근 HH를 일단 비교합니다 
# 거기서 사이에 존재한다면 이제 분을 비교합니다
# 그리고 초를 비교합니다

c=["09:12:23 11:14:35","10:34:01 13:23:40","10:34:31 11:20:10"]

b=input("머물렀던 인원을 알고싶은 시간을 입력하세요 : ")

count=0
for i in c:
    if int(i[:2])*3600+int(i[3:5])*60+int(i[6:8])<int(b[:2])*3600+int(b[3:5])*60+int(b[6:8])<int(i[9:11])*3600+int(i[12:14])*60+int(i[15:]):
        count+=1
    elif int(i[:2])*3600+int(i[3:5])*60+int(i[6:8])==int(b[:2])*3600+int(b[3:5])*60+int(b[6:8]) or int(b[:2])*3600+int(b[3:5])*60+int(b[6:8])==int(i[9:11])*3600+int(i[12:14])*60+int(i[15:]):
        count+=1

print(count)
'''
count=0
for a in c:
    print(a)
    if int(a[:2])<int(b[:2])<int(a[8:11]):
        count+=1
    elif a[:8]==b[:8] or a[9:]==b[:9]:
        count+=1
    elif int(a[:2])<int(b[:2]) and int(b[:2])==int(a[9:11]):  #시간 , #시간
        if int(b[3:5])<int(a[12:14]):  #분
            count+=1
        elif int(b[3:5])==int(a[12:14]):      #분
            if int(b[6:])<int(a[15:]):       #초
                count+=1 
    elif int(a[:2])==int(b[:2]):
        if int(a[3:5])<int(b[3:5]):
            count+=1
        elif int(a[3:5])==int(b[3:5]):
            if int(a[6:8])<int(b[6:]):
                count+=1

print(count)
    '''