num=int(input())
for i in range(1,num+1):
    for s in range(num,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
