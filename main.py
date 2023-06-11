class french:
    def say_hello(self):
        print("Bonjour")
        
class chinese:
    def say_hello(self):
        print("Ni hoe!")
        
def greet(lang):
    lang.say_hello()


Mike = french()
John = chinese()

greet(Mike)
greet(John)


# ------------------- Cars and Brand ---------------------


class cars:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        
    def car_details(self):
        return (f'{self.brand} and {self.model}')

car_1 = cars("Mistibushi", "Carisma")
car_2 = cars("Ford", "SUV")

print(car_2.car_details())
print(car_1.car_details())
