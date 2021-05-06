
def OneEditApart(s1,s2):
    cnt=0
    if abs(len(s1)-len(s2))>1:
        return "False"
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i] and s1[::-1][i]!=s2[::-1][i]:
            cnt+=1
    if cnt<=1:
        print("True")
    else:
        print("False")

OneEditApart("cat","ct")
