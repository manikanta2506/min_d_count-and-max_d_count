num=int(input())
s=0
j=0
while num: 
    r=num%10
    num=num//10
    s=s+r
if num==0:
    print(s)
    if s>9:
        k=s%10 
        j=s//10
        j=j+k
        print(j)
