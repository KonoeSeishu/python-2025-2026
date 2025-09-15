from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.refresh() # do umieszczenia w przestrzeni jedzenia

    def refresh(self): # gdy zjemy zjedzonko to pojawi sie w nowym miejscu
        shape = random.choice(["square", "circle", "triangle"])
        color = random.choice(["red", "green", "blue"])
        self.hideturtle() # ukrycie na czas przemieszczania
        self.shape(shape) # zmiana ksztaltu
        self.color(color) #zmiana koloru

        #losowy zakres pojawiania jedzonka
        self.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.showturtle()

    []

