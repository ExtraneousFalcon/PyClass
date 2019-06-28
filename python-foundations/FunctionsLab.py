import math
def age_calculator(age1,age2):
    return age1-age2
def avg_numbers(num1,num2,num3):
    return((num1+num2+num3)/3)
def avg():
    x = True
    sum = 0
    num = 0
    ave = 0
    print("Press N to get the average")
    while(x):
        a = input("Number: ")
        if(a!="N"):
            sum+=int(a)
            num+=1
            ave = sum/num
        else:
            x = False
    return ave

print(age_calculator(21,32))
print(avg_numbers(1,2,5))
print(avg())