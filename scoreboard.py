from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-275, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_scoreboard()

    def print_scoreboard(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.score + 1}", align='left', font=FONT)

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write('Gave over.', align='center', font=FONT)
