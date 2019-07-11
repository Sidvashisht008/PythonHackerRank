X=int(input())
Y=int(input())
Z=int(input())
N=int(input())
print([[a,b,c] for a in range(0,X+1) for b in range(0,Y+1) for c in range(Z+1) if a+b+c!=N])

