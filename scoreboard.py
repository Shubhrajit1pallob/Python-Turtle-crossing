from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 270)
        message = f"Level {self.level}"
        self.write(message, align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
