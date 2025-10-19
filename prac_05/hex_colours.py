"""
CP1404
Hexadecimal Colour
"""

COLOUR_TO_HEX = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "BEIGE": "#F5F5DC",
    "CORNFLOWERBLUE": "#6495ED",
    "CRIMSON": "#DC143C",
    "DARKGREEN": "#006400",
    "GOLD": "#FFD700",
    "INDIGO": "#4B0082",
    "LIGHTCORAL": "#F08080"
}

colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").upper()