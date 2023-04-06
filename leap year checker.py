year=int(input("enter the year:"))

if(year%400==0) and (year%100==0):
    print(year,"leap year")
elif(year%4==0) and(year%100!=0):
    print("leap year",year)
else:
    print("not a leap year")
