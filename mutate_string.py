def mutate_string(String,index,char):
    d=''
    for x in range(0,len(String)):
        if (x<index) or(x>index):
            d=d+String[x]
        else:
            d=d+char
    return(d)
