num,sv,rv=map(int,input().split())
rev=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
num=0
while rev:
    r=rev%10
    rev=rev//10
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    num=num*10+r

print(num)
