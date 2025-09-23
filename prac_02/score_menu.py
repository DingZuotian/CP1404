def get_valid_score():
    while True:
        score = float(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            return score
        print("Invalid score, try again.")


def get_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


def main():
    score = get_valid_score()

    while True:
        print("\nMenu: G - Get score, P - Print result, S - Show stars, Q - Quit")
        choice = input(">>> ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(get_score_status(score))
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()