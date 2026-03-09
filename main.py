from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen() 
screen.setup(600, 600) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
 
game_is_on = True

while game_is_on:               
    snake.move()
    time.sleep(0.1) 
    screen.update()
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()