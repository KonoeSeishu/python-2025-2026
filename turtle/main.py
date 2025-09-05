import turtle 
import time
import snake

window = turtle.Screen()
window.title("nya nya")
window.bgcolor("black")
window.setup(width=1920, height=1080)
turtle.color("white", "black")




def exit():
    turtle.bye()

def rotate_up():
    turtle.setheading(90)
    # turtle.fd(30)
    
def rotate_left():
    turtle.setheading(180)
    # turtle.fd(30)

def rotate_down():
    turtle.setheading(270)
    # turtle.fd(30)

def rotate_right():
    turtle.setheading(0)
    # turtle.fd(30)
    

turtle.onkey(rotate_up, "w")
turtle.onkey(rotate_left, "a")
turtle.onkey(rotate_down, "s")
turtle.onkey(rotate_right, "d")
turtle.onkey(exit, "space")



loop_delay = 0

turtle.listen()
window.tracer(0)



while True:
    window.update()
    time.sleep(0.001)
    loop_delay+=1
    
    while loop_delay==20:
        turtle.forward(movement_speed)
        print(str(turtle.xcor()))
        print(str(turtle.ycor()))
        loop_delay=0
    
#turtle.mainloop()
