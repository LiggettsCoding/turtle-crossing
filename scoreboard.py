from turtle import Turtle
import time


FONT = ("Courier", 24, "normal")
CURRENT_LEVEL = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-270, 255)
        # use this ^ times the added speed for added difficulty

    def first_level(self):
        global CURRENT_LEVEL
        CURRENT_LEVEL += 1
        self.write(f"Level {CURRENT_LEVEL}", font=FONT)

    def next_level(self):
        global CURRENT_LEVEL
        self.clear()
        CURRENT_LEVEL += 1
        self.write(f"Level {CURRENT_LEVEL}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-275, 230)
        self.write(f"GAME OVER!        level {CURRENT_LEVEL}", font=FONT)


class RoadLines(Turtle):
    def __init__(self):
        super().__init__()
        self.linecords = ((300, -262.5), (300, -237.5), (300, -212.5), (300, -187.5), (300, -162.5), (300, -137.5), (300, -112.5), (300, -87.5),
 (300, -62.5), (300, -37.5), (300, -12.5), (300, 12.5), (300, 37.5), (300, 62.5), (300, 87.5), (300, 112.5), (300, 137.5),
 (300, 162.5), (300, 187.5))

        self.setheading(180)
        self.color("black")
        self.penup()
        self.pensize(1)

    def make_roads(self):
        for cords in self.linecords:
            self.goto(cords)
            for n in range(1, 33):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)

