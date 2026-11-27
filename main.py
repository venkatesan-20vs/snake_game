import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


from PIL import Image
image = Image.open("snakehead.gif")

new_width = int(image.width * 0.025)
new_height = int(image.height * 0.025)

image = image.resize((new_width, new_height))
image.save("snakehead_small.gif")

image = Image.open("snakehead_small.gif")

image.rotate(0).save("head_right.gif")
image.rotate(90).save("head_up.gif")
image.rotate(180).save("head_left.gif")
image.rotate(270).save("head_down.gif")


screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.register_shape("snakehead_small.gif")
screen.register_shape("head_right.gif")
screen.register_shape("head_up.gif")
screen.register_shape("head_left.gif")
screen.register_shape("head_down.gif")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        score = score + 1
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        scoreboard.reset()
        snake.reset_snake()

    #collision with body
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset_snake()

