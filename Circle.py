import math
class Circle :
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
    
class calcCircle(Circle):
    def __init__(self, radius):
        super().__init__(radius)
choose = calcCircle(float(input("Enter radius of the circle: ")))
print(f"Area of the circle: {round(choose.area() , 2)}")
print(f"Circumference of the circle: {round(choose.circumference() , 2)}")
