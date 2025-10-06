"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file and return a list of lists: [subject, lecturer, number_of_students]."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Print all subject details in readable format."""
    for subject in subjects:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")


if __name__ == "__main__":
    main()