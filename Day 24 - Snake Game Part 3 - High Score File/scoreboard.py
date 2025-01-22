from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()


    #methods for files
    def write_highscore(self, high_score):
        with open("data.txt", "w") as file: #w write mode
            file.write(str(self.high_score))


    def read_high_score(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
            return self.high_score






