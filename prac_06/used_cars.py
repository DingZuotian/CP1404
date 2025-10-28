"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Example car
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # --- New code starts here ---
    # 1. Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # 2. Add 20 more units of fuel
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # 4. Attempt to drive the car 115 km
    limo.drive(115)

    # 5. Print the car object to test __str__ method
    print(limo)


main()