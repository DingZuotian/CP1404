import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in pick:
            pick.append(number)
    pick.sort()
    return pick

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

main()