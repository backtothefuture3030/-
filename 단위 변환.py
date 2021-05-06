
def cross(b,q):
    inch = {"cm" : 2.54, "pt" : 72, "px" : 96}
    cm = {"mm": 10 }
    pt = {"dxa": 20 }
    dxa = {"emu": 635}
    if b in inch:
        c= inch[b]*q   # 인치 속 단위의 수와 변환하고자 하는 수를 곱해줌
        print(c,b)
    elif b=="inch":
        print(q,b)
    elif b in cm:
        c = cm[b]*q*inch["cm"]
        print(c,b)
    elif b in pt:
        c = pt[b]*q*inch["pt"]
        print(c,b)
    elif b in dxa:
        c = dxa[b]*q*pt["dxa"]*inch["pt"]
        print(c,b)                  


def unit():
    A = input("변환 할 수를 입력하세요 : ")
    b = input("변환 할 단위를 입력하세요 : ")
    a = A.split() #a[0] 숫자 a[1] 단위
    inch = {"inch":int(a[0]),"cm":int(a[0])/2.54, "mm":int(a[0])/25.4, "px":int(a[0])/96, "pt":int(a[0])/72, "dxa":int(a[0])/1440, "emu":int(a[0])/914400}
    q = inch[a[1]]
    cross(b,q)

unit()
    
    
