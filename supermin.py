def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev

def findmin(n,data):
    s=min(data)
    r=reverse(s)
    for i in range(n):
        if data[i]==s:
            data[i]=r
        s=max(data)
        return s==r

n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(minval)
