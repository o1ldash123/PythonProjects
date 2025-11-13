print('Dog Breed Information Program')
class dog():
    def __init__(self, breed, size, color):
        self.breed = breed
        self.size = size
        self.color = color
        

    def info(self):
        return f"Breed: {self.breed}, Size: {self.size}, Color: {self.color}"
    
dog1 = dog("Labrador", "Large", "Yellow")
dog2 = dog("Beagle", "Medium", "Tricolor")
dog3 = dog("Chihuahua", "Small", "Fawn")
dog4 = dog("German Shepherd", "Large", "Black and Tan")

for d in (dog1, dog2, dog3, dog4):
    print(d.info())
    print(' ')