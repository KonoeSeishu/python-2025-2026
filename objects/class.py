class Car():
    def __init__(self, brand, name, year):
        self.brand = brand
        self.name = name
        self.year = year
        
    def printInfo(self):
        print(self.carName + " " + str(self.year))
        
    def changeYear(self, new_year):
        self.year = new_year
        
toyota = Car("Toyota", "Corolla", 2025)      
toyota.printInfo()

fiat = Car("Fiat", "Panda", 1999)
fiat.printInfo()
fiat.changeYear(2023)
fiat.printInfo()

suzuki = Car("Suzuki", "Vitara", 2025)
suzuki.printInfo()

