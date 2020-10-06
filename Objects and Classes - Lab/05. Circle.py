class Circle :
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return self.radius * self.__pi

    def calculate_area(self):
        return  ((self.diameter ** 2) * self.__pi) / 4

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * circle.__pi * self.radius * self.radius


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
