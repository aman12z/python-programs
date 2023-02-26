a=int(input("first number"))
b=int(input("second number"))
c=int(input("third number"))

largest=0

if(a>b and a>c):
   largest=a

if(b>a and b>c):
   largest=b

if(c>a and c>b):
   largest=c
print("the largest number between three number is=",largest)   
      
     
