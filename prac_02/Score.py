"""
CP1404/CP5632 - Practical
"""

def is_valid_score(score):
    return 0 <= score <= 100

def get_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    if not is_valid_score(score):
        print("Invalid score")
    else:
        status = get_score_status(score)
        print(status)

if __name__ == "__main__":
    main()