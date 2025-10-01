"""
CP1404/CP5632 - Practical
randoms.py - exploring the random module
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers:
# line 1 (random.randint(5, 20)):
#    -> Produced a random integer between 5 and 20 inclusive.
#    -> Smallest possible: 5
#    -> Largest possible: 20
#
# line 2 (random.randrange(3, 10, 2)):
#    -> Produced a random integer chosen from the sequence 3, 5, 7, 9
#    -> Smallest possible: 3
#    -> Largest possible: 9
#    -> Could it produce a 4? No, because step=2 means only odd numbers from 3 to 9.
#
# line 3 (random.uniform(2.5, 5.5)):
#    -> Produced a random floating-point number between 2.5 and 5.5
#    -> Smallest possible: 2.5 (inclusive)
#    -> Largest possible: 5.5 (inclusive)

# ---------------------------

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")