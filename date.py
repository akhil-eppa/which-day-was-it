import builtins
import math
#Hello World
x=True
while x:

    month=int(input("Enter the month(1-12) : "))
    while month<1 or month>12:
        month=int(input("Enter the month(1-12) : "))
    day=int(input("Enter the day(1-31) : "))
    while day<1 or day>31:
        day=int(input("Enter the day(1-31) : "))
    year=int(input("Enter the year(1800-2099) : "))
    while year<1800 or year>2099:
        year=int(input("Enter the year(1800-2099) : "))
    cent=year//100
    y=year%100
    value=y+math.floor(y/4)
    if cent==18:
        value=value+2
    elif cent==20:
        value=value+6
    if month==1 and not((year%4==0 and year%100!=0) or year%400==0):
        value=value+1
    elif month==2:
        if ((year%4==0 and year%100!=0) or year%400==0):
            value=value+3
        elif not((year%4==0 and year%100!=0) or year%400==0):
            value=value+4
    elif month==3 or month==11:
        value=value+4
    elif month==5:
        value=value+2
    elif month==6:
        value=value+5
    elif month==8:
        value=value+3
    elif month==10:
        value=value+1
    elif month==9 or month==12:
        value=value+6
    value=(value+day)%7
    if value==1:
        print("It is a Sunday")
    elif value==2:
        print("It is a Monday")
    elif value==3:
        print("It is a Tuesday")
    elif value==4:
        print("It is a Wednesday")
    elif value==5:
        print("It is a Thursday")
    elif value==6:
        print("It is a Friday")
    elif value==0:
        print("It is a Saturday")
    d=input("Do you want to check for another day? (y/n) : ")
    if d=="y":
        x=True
    else:
        print("Thankyou for using")
        x=False
