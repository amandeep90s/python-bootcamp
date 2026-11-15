# Exercise - Who will pay the bill

import random

friends = ["Alice", "John", "Robert", "Marco", "Richard"]

who_will_pay = random.randint(0, len(friends) - 1)

print(friends[who_will_pay])

# Second method
print(random.choice(friends))
