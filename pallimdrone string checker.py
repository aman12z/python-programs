# string pallimdrome or not

a= input("enter the word:")
rev = a[::-1]

if a == rev:
    print("palindrome string")
else:
    print("not palindrome")
