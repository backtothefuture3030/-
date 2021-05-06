count=0
for hour in range(0,24):
    for ang in [90, 270]:
        move = 360*hour+ang
        min = move/5.5
        hours = min//60
        if hours < 24:
            print("%02d:%02d"%(hours,min%60))
            count+=1
print(count)

        
            