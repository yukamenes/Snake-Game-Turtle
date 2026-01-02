from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def create_turtle():
    t = Turtle()
    t.shape("square")
    t.color("white")
    return t

def start_position_of_turtle(t, x , y):
    t.up()
    t.goto(x, y)

segments = [create_turtle() for _ in range(3)]


start_position_of_turtle(segments[0], 0, 0)
start_position_of_turtle(segments[1], -20, 0)
start_position_of_turtle(segments[2], -40, 0)

game_is_on = True

while game_is_on:               
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].fd(20)
    time.sleep(0.1) 
    screen.update()











screen.exitonclick()