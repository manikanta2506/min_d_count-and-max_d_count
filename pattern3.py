num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        if i%2==1:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
