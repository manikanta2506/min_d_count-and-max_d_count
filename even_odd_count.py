num=int(input())
oc=0
ec=0
while num:
    r=num%10
    num=num//10
    if r%2:
        oc+=1
    else:
        ec+=1
if oc%2==1 and ec%2==0:
    print("Even Odd")
elif ec%2==0:
    print("even")
elif oc%2:
    print("Odd")
else:
    print("mixed")
