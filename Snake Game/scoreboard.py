from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score {self.score} Highscore {self.highscore}", align="center",
                   font=("Arial", 24, "normal"))
        
    def reset(self):
        if self.score > self.highscore
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align="center",
                   #font=("Arial", 24, "normal"))
