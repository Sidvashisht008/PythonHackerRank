n=int(input())
A=[]
B=[]
A=list(map(int,input().split()))
for i in A:
    if i not in B:
        B=B+[i]
A=B
A=sorted(A)
print(A[len(A)-2])
