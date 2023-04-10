#check input year is leap year
year=int(input("ENTER YEAR:"))
if(year%100!=0):
    if year%4==0:
       print("IT'S A LEAP YEAR")
    else:
       print("IT'S NOT A LEAP YEAR")
else:
    if year%400==0:
        print("IT'S A LEAP YEAR")
    else:
       print("IT'S NOT A LEAP YEAR")



#check input year is leap year
year=int(input("ENTER YEAR:"))
if(year%100!=0 and year%4==0):
       print("IT'S A LEAP YEAR")
elif year%400==0:
       print("IT'S A LEAP YEAR")
else:
       print("IT'S NOT A LEAP YEAR")
