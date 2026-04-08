"""
Main module for the Snake Game.

Initializes the game window, creates all game objects,
handles user input, and runs the main game loop.

Includes:
- collision detection (food, walls, tail)
- dynamic scoring system
- automatic game reset with high score tracking
"""

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Create and configure the game screen
screen = Screen() 
screen.setup(600, 600) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Create game objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Bind keyboard keys to snake movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
 
game_is_on = True

# Main game loop
while game_is_on:               
    snake.move()
    time.sleep(0.1) 
    screen.update()

    # Check collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        # Assign points depending on food color
        if food.color()[0] == "red":
            points = 1
        elif food.color()[0] == "green":
            points = 2
        elif food.color()[0] == "yellow":
            points = 3
        elif food.color()[0] == "orange":
            points = 4

        scoreboard.increase_score(points)

    scoreboard.update_scoreboard()

    # Check collision with wall
    if (
        snake.head.xcor() >= 280
        or snake.head.xcor() <= -280
        or snake.head.ycor() >= 280
        or snake.head.ycor() <= -280
        ):
        scoreboard.reset()
        snake.reset()
    
    # Check collision with snake tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()