#Elvis Nguyen
class book():
    def __init__(self, book: str, price: float, quantity: int):
        self.book = book
        self.price = price
        self.quantity = quantity

    #getter methods
    def getBook(self):
        return self.book

    def getPrice(self):
        return str("$"+self.price)

    def getQuantity(self):
        return self.quantity

    #setter methods    
    def setBook(self, newBook: str):
        self.book = newBook

    def setPrice(self, newPrice: float):
        self.price = newPrice

    def setQuantity(self, newQuantity: int):
        self.quantity = newQuantity

    #String Method
    def __str__(self):
        return f"Book: {self.book} | Price: {self.price} | Quantity: {self.quantity}"
    
    #sell copies
    def sellCopies(self, quantity):
        self.quantity -= quantity
