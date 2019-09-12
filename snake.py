from turtle import *
import turtle
from random import randrange
from freegames import square, vector
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
screen = turtle.Screen()
def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    screen.title('MiniSnake SCORE: {}'.format(len(snake)))

    if len(snake)<5:
        ontimer(move, 100)
    elif len(snake)>5 or len(snake)<20:
        ontimer(move, 75)
    elif len(snake)>20 or len(snake)<50:
        ontimer(move, 50)
    elif len(snake)>50:
        ontimer(move, 35)
setup(420, 420, 370, 0)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
