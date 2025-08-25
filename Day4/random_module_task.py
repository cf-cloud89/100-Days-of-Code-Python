import random

print("Welcome to the Coin Flip Game!")

random_number = random.randint(0, 1)
# print(random_number)

if random_number == 0:
    print("Heads")
else:
    print("Tails")


# random_number = random.randint(0, 10) * 10
# print(random_number)
#
# if 0 <= random_number <= 10:
#     print("Heads")
# else:
#     print("Tails")
