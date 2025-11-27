"""
CP1404/CP5632 Practical
Wikipedia lookup
"""

import wikipedia


def main():
    """Get a page title from the user and show details from Wikipedia."""
    # First prompt
    search_phrase = input("Enter page title (or blank to quit): ")

    while search_phrase != "":
        try:
            # Try to get the page with this exact title
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"\nTitle: {page.title}")
            print(f"URL  : {page.url}")
            print("Summary:")
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            # When the title is too vague or has many meanings
            print("That title is ambiguous. Here are some options:")
            for option in e.options[:10]:  # only show first few
                print(f"- {option}")
        except wikipedia.exceptions.PageError:
            # When no page exists with that title
            print("Page not found. Please try another title.")

        print()  # blank line for readability
        search_phrase = input("Enter page title (or blank to quit): ")

    print("Goodbye")



if __name__ == "__main__":
    main()