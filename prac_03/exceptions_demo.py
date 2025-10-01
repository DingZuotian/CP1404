"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Q1:
# A ValueError will occur if a function receives a valid type but an invalid value, for example: using random.randrange() with step=0, or with start >= stop, or an invalid string format specifier.
#Q2:
# A ZeroDivisionError will occur if the program tries to divide by zero, for example, using an expression like x / 0 or dividing by a random value that could be 0.
#Q3:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (cannot be 0): "))
    while denominator == 0:
        print("Denominator cannot be zero. Try again.")
        denominator = int(input("Enter the denominator (cannot be 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")