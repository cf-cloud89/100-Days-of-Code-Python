print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")



print("Welcome to the Cafe!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("Welcome!")

    age = int(input("What is your age?"))

    if age <= 15:
        print("Your coffee price is $7.")
    elif age <= 18:
        print("Your coffee price is $10.")
    elif age <= 25:
        print("Your coffee price is $15.")
    else:
        print("You coffee price is $20.")
else:
    print("You cannot use the rollercoaster.")
