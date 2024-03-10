from turtle import Turtle
ALIGNEMNT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNEMNT, font=FONT)
    

    def add_to_score(self):
        self.score = self.score + 1
        self.write_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNEMNT, font= FONT)

    
    def reset(self):
        if self.high_score > self.score:
            self.high_score = self.score
        self.score = 0
        self.write_score()