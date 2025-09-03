class Radio():
    def __init__(self, brand, frequency, volume, ison=False):
        self.brand = brand
        self.frequency = frequency
        self.volume = volume
        self.ison = ison
    
    def turnOn(self):
        self.ison = True
        
    def turnOff(self):
        self.ison = False
    
    def getRadioInfo(self):
        return f"Brand {self.brand}, frequency, {self.frequency}, volume {self.volume}"
    
radio1 = Radio("Sony", 101.2, 5)
print(radio1.getRadioInfo())
radio2 = Radio("Philips", 98.7, 7)
print(radio2.getRadioInfo())