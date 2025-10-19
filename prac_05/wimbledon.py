"""
CP1404
Wimbledon
"""

FILENAME = "wimbledon.csv"

def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        file.readline()
        records = [line.strip().split(",") for line in file]

    champions = {}
    countries = set()

    for record in records:
        countries.add(record[1])
        champions[record[2]] = champions.get(record[2], 0) + 1

    print("Wimbledon Champions:")
    for name, wins in sorted(champions.items()):
        print(f"{name:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()