from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()


    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)


    def increase_score(self, player):
        """Increases scores based on parameters l and r (left and right)"""
        if player == "l":
            self.l_score += 1
            self.update()
        if player == "r":
            self.r_score += 1
            self.update()



