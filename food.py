"""
Food module.

Contains the Food class which represents the food object
that the snake can eat to gain points and grow longer.
"""

from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "orange"]


class Food(Turtle):
    """
    Represents the food in the Snake Game.

    The food appears at random positions and changes color,
    which determines how many points the player receives.
    """

    def __init__(self):
        """Initialize the food object with a random color and position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        """
        Move the food to a new random position
        and assign it a new random color.
        """
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)