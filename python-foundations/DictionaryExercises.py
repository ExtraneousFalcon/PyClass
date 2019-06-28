def polling_friends():
    fav_animals = {
        "Miranda": input("Miranda, what is your favorite animal? "),
        "Gordo": input("Gordo, what is your favorite animaL? ")
    }
    return fav_animals
print(polling_friends())

def birthday_month(current, birthday):
    months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    curNum = months[current]
    birNum = months[birthday]
    return (birNum-curNum)%12
print(birthday_month("September", "May"))
