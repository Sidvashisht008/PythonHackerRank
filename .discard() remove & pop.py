n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(1,N+1):
    a=input()
    if a=="pop":
        s.pop()
#     elif a.split()[0]=='discard':
#         s.discard(int(a.split()[1]))
#     elif a.split()[0]=="remove":
#         s.remove(int(a.split()[1]))
print(sum(list(s)))
