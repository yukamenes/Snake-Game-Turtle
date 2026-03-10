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
        self.write(f"Score: {self.score}", 
                   align=ALIGNMENT, 
                   font=FONT)

    def game_over(self):
        """Display the 'GAME OVER' message in the center of the screen."""
        self.goto(0,0)
        self.write("GAME OVER", 
                   align=ALIGNMENT, 
                   font=FONT)