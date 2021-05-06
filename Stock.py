

def Stock(a):
    if 100<=a<=10000:
        b=int(input("투자기간을 입력하세요 :"))
        if 1<=b<=10:
            d=a
            i=0
            while  i<b:
                c=int(input("변동폭 입력 :"))
                if -100<=c<=100:
                    a*=(1+float(c/100))
                    i+=1
                else:
                    print("변동폭 오류")
                    return False
            print(int(a)-d)
            if int(a)-d>0:
                print("good")
            elif int(a)-d==0:
                print("same")
            else:
                print("bad")
        else:
            print("투자기간을 다시설정하세요")
    else:
        print("투자액을 다시 설정하세요")

Stock(int(input("투자액을 입력하세요 : ")))
