import turtle

class Snake:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    MOVE_DISTANCE = 20

    def __init__(self, startX, startY):
        self.startX = startX
        self.startY = startY
        self.segments = [] #segmenty snake
        self.refresh()

    def refresh(self): #przy jej wykonaniu tworzymy weza od nowa
        print("snake reset")
        for seg in self.segments: #po restarcie wyrzuca poza ekran startowy
            seg.goto(2000, 2000)
        self.segments.clear()

        self.addSegment(self.startX, self.startY)
        self.head = self.segments[0] #wskazujemy ktory segment jest głowa
        self.direction = None #informacja w ktoorym kierunku porusza sie waz

    def addSegment(self, x, y): # metoda dodawania poczatkowego segmentu weza
        t = turtle.Turtle("square") # tworzenie weza - poczotkowy kwadrat
        t.hideturtle()  # ukrycie weza przy tworzeniuq
        t.penup()
        t.speed(0)
        t.goto(x, y)
        t.color("green")
        t.showturtle()
        self.segments.append(t)

    def extend(self): #metoda dodajaca segment do weza po zjedzeniu robaczka
        self.addSegment(1000,1000)

    def keyUP(self): #metoda za pomoca ktorej okreslamy gdzie waż ma podazac automatycznie
        self.direction = Snake.UP

    def keyDOWN(self):
        self.direction = Snake.DOWN

    def keyLEFT(self):
        self.direction = Snake.LEFT

    def keyRIGHT(self):
        self.direction = Snake.RIGHT

    def move(self):
        headX = self.head.xcor()
        headY = self.head.ycor()

        if self.direction == Snake.UP:
            headY += Snake.MOVE_DISTANCE

        if self.direction == Snake.DOWN:
            headY -= Snake.MOVE_DISTANCE

        if self.direction == Snake.LEFT:
            headX -= Snake.MOVE_DISTANCE

        if self.direction == Snake.RIGHT:
            headX += Snake.MOVE_DISTANCE

        index = len(self.segments) - 1
        while index > 0:
            newX = self.segments[index - 1].xcor()
            newY = self.segments[index - 1].ycor()
            self.segments[index].goto(newX, newY)
            index -= 1

        self.head.goto(headX, headY)

    def checkSelfCollision(self):
        for seg in self.segments:
            if seg == self.head:
                continue
            elif self.head.distance(seg) < 20:
                return True
        return False

    def checkWallCollision(self, screenWidth, screenHeight):
        halfWidth = screenWidth / 2
        halfHeight = screenHeight / 2;
        x = self.head.xcor()
        y = self.head.ycor()

        if x > halfWidth or x < - halfWidth or y > halfHeight or y < -halfHeight:
            return True
        else:
            return False




