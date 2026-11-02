print("Welcome to Rollercoaster ride")

height = int(input("Please enter you height in cm: "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter you age in years: "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can not ride the rollercoaster")
