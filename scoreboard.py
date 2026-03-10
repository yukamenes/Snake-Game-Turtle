from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier New', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.speed("fastest")
        self.score = 0
    
    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", 
                   align=ALIGNMENT, 
                   font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", 
                   align=ALIGNMENT, 
                   font=FONT)

    
