def wrap(string, max_width):
    b=""
    for i in range(0,len(string),max_width):
        a=string[i:i+max_width]
        b=b+a+"\n"
    return(b)
