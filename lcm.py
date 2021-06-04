a,b=map(int,input().split())
t=2
s=1
while t<=a and t<=b:
      if a%t==0 and b%t==0:
          a=a//t
          b=b//t
          s=s*t
      else:
          t+=1
s=s*a*b
print(s)
