"""
Snake module.

Contains the Snake class responsible for creating the snake,
moving it, growing it, and controlling its direction.
"""

from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
LEFT = 180
RIGHT = 0
UP = 90


class Snake():
    """
    Represents the snake in the Snake Game.

    The snake consists of multiple turtle segments that move together.
    """

    def __init__(self):
        """Initialize the snake with starting segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        """Create the initial snake body using predefined positions."""
        for pos in START_POSITION:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        """
        Create a new snake segment.

        Args:
            pos (tuple): The (x, y) position where the new segment will appear.
        """
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.up()
        segment.goto(pos)
        self.segments.append(segment)
    
    def extend(self):
        """Add a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the snake forward.

        Each segment moves to the position of the segment in front of it,
        while the head moves forward by MOVE_DISTANCE.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)
    
    def up(self):
        """Change snake direction to up if it is not currently moving down."""
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        """Change snake direction to down if it is not currently moving up."""
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def left(self):
        """Change snake direction to left if it is not currently moving right."""
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
    def right(self):
        """Change snake direction to right if it is not currently moving left."""
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def reset(self):
        for seg in self.segments:
            seg.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]