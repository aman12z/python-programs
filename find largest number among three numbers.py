num1=int(input("number one"))
num2=int(input("number two"))
num3=int(input("number three"))

if (num1 > num2 ) and (num1 > num3):
    print("the largest number",num1)

elif (num2 > num1 ) and (num2 > num3) :
    print("the largest number",num2)

else:
    print("the largest number",num3)
