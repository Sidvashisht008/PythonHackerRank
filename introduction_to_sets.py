def average(array):
    B=[]
    for i in array:
        B=B+[int(i)]
    B=list(set(B))
    return(float(sum(B)/len(B)))
