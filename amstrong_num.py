def isamstrong(num):
    temp=num
    c=0
    while temp:
        temp=temp//10
        c+=1
    res=0
    temp=num
    while temp:
        r=temp%10
        temp=temp//10
        res=res+pow(r,c)
    if res==num:
        return True
    return False


num=int(input())
print(isamstrong(num))
