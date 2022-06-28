from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()

    def increase_score(self):
        self.level += 1

    def update_level(self):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def finished_game(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
