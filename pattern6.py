num=int(input())
for i in range(1,num+1):
    if i%2:
        temp=1
    else:
        temp=0
    for j in range(1,num+1):
        print(temp,end="")
        if temp==0:
            temp=1
        else:
            temp=0
    print()
