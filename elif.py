age = int(input("How old are you?"))

if age < 0:
    print("That age doesn't exist")
elif age >= 0 and age <= 6:
    print("You are in the range 0-6 ")
elif age >= 7 and age <= 10:
    print("You are in the age range 7-10")
elif age >= 11 and age <= 15:
    print("You are in the age range 11-15")
elif age >= 16 and age <= 20:
    print("You are in the range 16-20")
else:
    print("You are older than 20.")