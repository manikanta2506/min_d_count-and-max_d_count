def isfib(num):
    if num==0 or num==1:
        return True
    a=0
    b=1
    c=0
    while c<=num:
        c=a+b
        count+=1
        a=b
        b=c
    print(count,end=" ")
    return False

num=int(input())
print(isfib(num))
    
