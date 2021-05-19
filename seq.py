n=int(input())
while n!=1:
    if n==1:
        break
    if n%2==0:
        n=n//2
        print(n,end=" ")
    else:
        n=3*n+1
        print(n,end=" ")
