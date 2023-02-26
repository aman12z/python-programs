n=int(input("enter the number you like most"))


fact=1

if(n<0):
    print("factorial doesn't exist for negative number")
elif(n==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("the factorial =",n,"is",fact )    
