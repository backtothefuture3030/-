'''
당신은 상식은행의 입출금 처리 프로그램을 만들고 있다. 상식은행의 입출금 요청 입력 양식에는 금액을 입력하는 난이 있다. 
이 난은 한국식 통화 표기법으로 입력하도록 되어 있다. 한국식 통화 표기법은 한국인이 흔히 사용하는 구두식 표현으로, 다음과 같은 방식이다.
'''



def korean_number(string):
    count_dict = {"일":1,"이":2,"삼":3,"사":4,"오":5,"육":6,"칠":7,"팔":8,"구":9,"십":10,"백":100,"천":1000,"만":10**4,"억":10**8,"조":10**12,"경":10**16}
    a_list = ["일","이","삼","사","오","육","칠","팔","구"]
    b_list = ["십","백","천"]
    c_list = ["만","억","조","경"]

    if string == "영":
        return 0
    else:
        data = list(string)
        subtotal = 0
        total = 0
        a = 0
        for i in range(len(data)):
            count = count_dict.get(data[i])            
            if data[i] in a_list:
                a = count
            if data[i] in b_list:
                b = count
                if a == 0:
                    a = 1
                if data[i] == data[-1] == "천" and total >= 10**8:
                    subtotal = a * b * 10000
                else:
                    subtotal += a * b
                a = 0
            if data[i] in c_list:
                c = count
                if subtotal == 0 and a == 0:
                    if c == "만":
                        a = 1
                    else:
                        return False
                if subtotal == 0:
                    total += a * c
                    a = 0
                else:
                    total += (subtotal + a) * c
                    subtotal = 0
                    a = 0

        total = total + subtotal + a

    return total

string = input("판단할 화폐를 입력하세요")
print(korean_number(string))