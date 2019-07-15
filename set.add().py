N=int(input())
L=[]
for i in range(1,N+1):
    a=input()
    L+=[a]
print(len(list(set(L))))
