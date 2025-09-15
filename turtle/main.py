import time,turtle
from snake import *
from food import *


window = turtle.Screen()
window.title("Snake")
width = 700
height = 700
window.setup(width, height)
window.bgcolor("yellow")

snake = Snake(0, 0)
window.listen() #nasluchujemy klawiature

window.onkey(snake.keyUP, "Up") #przekazujemy przyciski ktore chcemy nasluchiwac
window.onkey(snake.keyDOWN, "Down")
window.onkey(snake.keyLEFT, "Left")
window.onkey(snake.keyRIGHT, "Right")
window.onkey(snake.keyUP, "w")
window.onkey(snake.keyDOWN, "s")
window.onkey(snake.keyLEFT, "a")
window.onkey(snake.keyRIGHT, "d")
food = Food()
while True:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.checkSelfCollision() or snake.checkWallCollision(width, height):
        food.refresh()
        snake.refresh()
