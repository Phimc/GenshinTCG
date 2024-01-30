def change(count,flag,max_limit=10):
    #count.value = 4
    if flag == '+' and count.value<max_limit:
        count.value+=1
    elif flag == '-' and count.value>0:
        count.value-=1