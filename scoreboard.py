"""
Scoreboard module.

Contains the ScoreBoard class responsible for displaying
the player's score and the game over message.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier New', 20, 'normal')


class ScoreBoard(Turtle):
    """
    Displays the current score and game status on the screen.
    """

    def __init__(self):
        """Initialize the scoreboard and place it at the top of the screen."""
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.high_score = self.read_score_from_file()

    
    def read_score_from_file(self):
        with open("data.txt") as file:
            score = int(file.read())
        return score

    def save_score_to_file(self, high_score):
        with open("data.txt", "w") as file:
            file.write(str(high_score))


    def increase_score(self, points):
        """
        Increase the player's score.

        Args:
            points (int): Number of points to add to the score.
        """
        self.score += points

    def update_scoreboard(self):
        """Clear the previous score and display the updated score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", 
                   align=ALIGNMENT, 
                   font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score_to_file(self.high_score)
        self.score = 0
        self.update_scoreboard()
