M=input()
A=set(list(map(int,input().split())))
N=input()
B=set(list(map(int,input().split())))
D=[list(A.difference(B)),list(B.difference(A))]
j=0
O=[]
for i in range(0,len(D)):
    for j in range(0,len(D[i])):
        O=O+[D[i][j]]
O=sorted(O)
for i in O:
    print(i)



