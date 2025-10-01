name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())

print(first_number + second_number)

with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line.strip())

print(total)