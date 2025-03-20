"""Avoid, classic arcade game.

Exercises

1. Display the duration of the game.
2. Vary the size of the bombs.
3. Vary the speed of the bombs.
"""

from random import choice, randrange
from turtle import (
    clear, goto, dot, update, ontimer, setup, hideturtle, up,
    tracer, listen, onkey, done
)

from freegames import vector

north, south = vector(0, 4), vector(0, -4)
east, west = vector(4, 0), vector(-4, 0)
options = north, south, east, west

player = vector(0, 0)
aim = choice(options).copy()
bombs = []
speeds = []


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()
    goto(player.x, player.y)

    if alive:
        dot(10, "blue")
    else:
        dot(10, "red")

    for bomb in bombs:
        goto(bomb.x, bomb.y)
        dot(20, "black")

    update()


def move():
    """Update player and bomb positions."""
    player.move(aim)

    for bomb, speed in zip(bombs, speeds):
        bomb.move(speed)

    if randrange(10) == 0:
        speed = choice(options).copy()
        spawn_offset = randrange(-199, 200)

        if speed == north:
            bomb = vector(spawn_offset, -199)
        elif speed == south:
            bomb = vector(spawn_offset, 199)
        elif speed == east:
            bomb = vector(-199, spawn_offset)
        else:
            bomb = vector(199, spawn_offset)

        bombs.append(bomb)
        speeds.append(speed)

    for i, (bomb, speed) in enumerate(zip(bombs, speeds)):
        if not inside(bomb):
            del bombs[i]
            del speeds[i]

    if not inside(player):
        draw(False)
        return

    for bomb in bombs:
        if abs(bomb - player) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()

onkey(lambda: aim.set(north), "Up")
onkey(lambda: aim.set(south), "Down")
onkey(lambda: aim.set(east), "Right")
onkey(lambda: aim.set(west), "Left")

move()

if __name__ == "__main__":
    done()
