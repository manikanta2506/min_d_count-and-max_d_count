from math import *
l,b=map(float,input().split())
area=l*b
peri=2*(l+b)
dia=sqrt(l**2+b**2)
print("%.2f"%area,end=" ")
print("%.2f"%peri,end=" ")
print("%.2f"%dia,end=" ")
