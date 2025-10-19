"""
CP1404
Emails
"""

def get_name_from_email(email):
    """Extract a possible name from the given email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


def main():
    """Store users' emails and names in a dictionary, then print them."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()