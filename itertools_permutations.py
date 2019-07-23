from itertools import permutations
S,k=input().split()
k=int(k)
l=[]
perm=list(permutations(S,k))
for i in perm:
    l=l+["".join(i)]
for i in sorted(l):
    print(i)
