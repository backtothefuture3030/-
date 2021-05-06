'''
>>> aa = {1:"안녕"}
>>> aa[2] = "하이"
>>> aa
{1: '안녕', 2: '하이'}
>>> 
>>> aa[3] = "방가"
>>> aa
{1: '안녕', 2: '하이', 3: '방가'}
>>> aa["인사"]="굿모닝"
>>> aa
{1: '안녕', 2: '하이', 3: '방가', '인사': '굿모닝'}
>>> aa[3]=[1,2,3]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝'}
>>> aa[age]=23
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    aa[age]=23
NameError: name 'age' is not defined
>>> aa["age"]=23
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝', 'age': 23}
>>> aa[0]="adf"
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝', 'age': 23, 0: 'adf'}
>>> 
>>> 
>>> del aa[0]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝', 'age': 23}
>>> del aa[44]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del aa[44]
KeyError: 44
>>>

딕셔너리 주의사항
--key값(지수)은 고유한 값이므로 중복되는 값을 설정 놓으면 안된다.
만약 중복이 된다면 하나만 적용되고 나머지는 제외된다.

키값으로 리스트는 쓸 수 없다. 튜플은 키 값으 사용 가능하다.
키값은 값이 변할 수 없다는 전제하에 타입 설정하면된다.



dict() 함수




'''

aa = dict() #항목(key:value)이 없는 딕셔너리를 만든다.

print(aa)

aa['one'] = "첫번째"
print(aa)

#key 리스트를 만드는 함수 (keys())
bb = {"name":"홍길동", "hp":"010-1234-1234", "age":23}
keylist = bb.keys()  #리턴객체는 dict_keys 쉘에서 이렇게뜸
print(keylist)

print(bb['name'])
for key in bb.keys(): #dict_keys 객체의 각 요소값을 출력
    print(key)

cc = list(bb.keys()) #dict_keys 객체 리스트로 변환
print(cc)

#valueList 를 만드는 함수 (values())

valuelist= bb.values() #리턴값은 dict_values객체이다.
print(valuelist)

#key와 value 한쌍(항목)을 얻기(items())

item = bb.items()   #리턴값은 dict_items객체이다. 이 객체의 요소 튜플로 구성된다.
              #참고  #dict_items객체 : [('name', '홍길동'), ('hp', '010-1234-1234'), ('age', 23)]
print(item)

# key : value 쌍을 모두 삭제하기(clear())
# bb.clear()
# print(bb)

#key값을 이용하여 value를 얻어오기(get)

q = bb.get('age')
print(q)

age = bb['age'] #get함수를 이용하지 않고 사용하는 방법
print(age)

'''
gender = bb['gender'] 이때 키값이 존재하지 않으면 에러처리가 난다.  
print(gender)'''

#get()함수는 키값이 존재하지 않을 경우에는 None값을 리턴한다.
gender = bb.get('gender')
print("======get 함수 실행후 bb 딕셔너리 =====")
print(gender)
print(bb)

#딕셔너리내에 키값이 없을 경우 디폴트값을 주는 방법
gender = bb.get("gender",'디폴트값')
print(gender)

#딕셔너리내에 해당 키가 존재하는지 알아보기 (in)
confirm_bb ='gender' in bb
print(confirm_bb)

confirm_bb='name' in bb
print(confirm_bb)

#pop() 함수를 이용해서 value값을 가져오기: 딕셔너리에 항목을 제거한다.
m = bb.pop('name')
print(m)
print("=======pop함수 실행후 bb 딕셔너리=====")
print(bb)

bb["name"] = "홍길동"
print(bb)

m = bb.pop('gender','없음') #key가 없는 경우에는 디폴트값으로 대체
 #pop(key [,디폴트값])으로 쓸수있다. 
print(m)

length = len(bb) #딕셔너리의 항목 갯수를 구함
print(length)




