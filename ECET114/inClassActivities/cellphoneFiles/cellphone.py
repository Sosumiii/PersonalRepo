class CellPhone():
    def __init__(self, manufacturer, model, price):
        
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def getManufacturer(self):
        return self.manufacturer

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price
    
    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def setModel(self, model):
        self.model = model

    def setPrice(self, price):
        self.price = price

    def raisePrice(self, percentage):
        self.price = self.price * (1+percentage)

    def reducePrice(self, percentage):
        self.price = self.price * (1-percentage)

    def __str__(self):
        msg = f"info: Manufacturer: {self.manufacturer}, Model: {self.model}, Price: ${self.price:.2f}"
        return msg