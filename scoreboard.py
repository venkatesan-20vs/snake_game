from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Press Start 2P", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as high:
            self.highscore = int(high.read())
        self.color("#FFD700")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as high:
                high.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER\nYOUR SCORE: {self.score}", align=ALIGNMENT, font=FONT)
