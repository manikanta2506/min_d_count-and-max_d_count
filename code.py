
num=int(input())
temp=num
ma=0
mi=9
c1=0
c2=0
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    elif r<mi:
        mi=r
print(mi,ma)
while temp:
    a=temp%10
    temp=temp//10#1
    if a==ma:#1==1
        c1=c1+1#c1=1
    elif a==mi:
        c2=c2+1
print(c2,c1)
"""
num=int(input())
temp=num
mi=9
ma=0
c=0
d=0
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    elif r<mi:
        mi=r
print(mi,ma)
while temp:
    r=temp%10
    temp=temp//10
    if r==ma:
        c=c+1
    elif r==mi:
        d=d+1
print(d,c)
"""
