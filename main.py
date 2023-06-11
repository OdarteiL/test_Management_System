class cars: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    
    def car(self):
        return (f'{brand} : {model}')


Japan_car = cars("Honda", "civic")

Japan_car.car()