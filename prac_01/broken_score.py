"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

def get_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    try:
        score = float(input("Enter score: "))
    except ValueError:
        print("Invalid score")
        return
    print(get_score_status(score))

if __name__ == "__main__":
    main()