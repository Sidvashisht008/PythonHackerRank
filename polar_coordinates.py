import math,cmath
a=complex(input())
r=math.sqrt(a.real**2+a.imag**2)
q=cmath.phase(complex(a.real,a.imag))
print(r)
print(q)
