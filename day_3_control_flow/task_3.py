print("Welcome to Rollercoaster ride")

height = int(input("Please enter you height in cm: "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter you age in years: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you want to have a photo take? Type y for Yes or n for No. ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is: {bill}")
else:
    print("You can not ride the rollercoaster")
