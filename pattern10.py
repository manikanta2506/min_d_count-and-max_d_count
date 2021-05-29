num=int(input())
for i in range(1,num+1):
    if i%2:
        t=1
    else:
        t=t-2
    for j in range(num,i-1,-1):
        if i%2:
            print(t,end="")
            t+=1
        else:
            print(t,end="")
            t-=1
    print()
