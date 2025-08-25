# Option No1

import random
friends = random.choice(["Alice", "Bob", "Charlie", "David", "Emanuel"])
print(friends)


# Option No2
# import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
bill_payer = random.choice(friends)
print(f"The person that will pay the bill is: {bill_payer}")


# Option No3 (Angela Yu)
# import random
random_numb = random.randint(0, 4)
print(friends[random_numb])
