num = int(input("enter the number:"))

fact=1

if num<0:
    print("factorial of 0 doesn't exist")

if num==0:
    print("factorialof 0 is ",1)

if num > 0:
    for i in range (1,num+1):
        fact = fact*i
print("the factorial is ",fact)



#by recursion
def fact (a):
     if a==0:
         return 1
     else:
         return (a)*fact(a-1)
num = int(input("enter the number"))        
result=fact(num)
print("the factorial is",result)
