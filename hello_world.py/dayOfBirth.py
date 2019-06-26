import datetime
today = datetime.datetime.now()
print("Enter your date of birth in the given order")
dD = input('Enter date of day')
mD = input('Enter date of month')
yD = input('Enter year of month')
num = datetime.datetime(int(yD),int(mD),int(dD),1,1,1).weekday()
print('Your day of birth is', end=" ")
if num==0:
    print("Monday")
elif num==1:
    print("Tuesday")
elif num==2:
    print("Wednesday")
elif num==3:
    print("Thursday")
elif num==4:
    print("Friday")
elif num==5:
    print("Saturday")
elif num==6:
    print("Sunday")