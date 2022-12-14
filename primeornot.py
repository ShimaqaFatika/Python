n=int(input("Enter a number: "))
flag=0
for i in range(1,n+1):
    if(n%i==0):
        flag=flag+1
if(flag==2):
    print("The given number is prime")
else:
    print("The give number is not prime")
