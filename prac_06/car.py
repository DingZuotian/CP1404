class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel):
        """Initialise a Car instance with a name and amount of fuel."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add the given amount of fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if enough fuel is available."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car using f-string formatting."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"