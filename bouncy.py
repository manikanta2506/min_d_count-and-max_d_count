def isbouncy(n,data):
    if data[0]<data[1]:
        h=True
        l=False
    else:
        l=True
        h=False
    for i in range(1,n-1):
        if (h==1 and data[i]<data[i+1]) or (l==1 and data[i]>data[i+1]):
            return False
        h=not h
        l=not l
    return True
n=int(input())
data=list(map(int,input().split()))
print(isbouncy(n,data))
            
