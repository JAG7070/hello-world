from graphics import *
from my_turtle import MyTurtle
from random import uniform

WIN_WIDTH = 700
WIN_HEIGHT = 600

RAND_ANGLE_MAX = 30
RAND_FACTOR_MAX = 0.2

wn = GraphWin("Simple tree", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
tree = MyTurtle(wn, 50, 50, 0)
angle = 5
dividend = 1.4


def clear(win):
    "More description added. And another one."
    for item in win.items[:]:
        item.undraw()
    # win.update()


def branch(length, use_randomness=True):
    if length < 2:
        return

    tree.forward(length)

    pos = tree.pos()
    heading = tree.heading()

    # randomness
    rand_angle_r = 0.0
    rand_factor_r = 1.0
    rand_angle_l = 0.0
    rand_factor_l = 1.0
    if use_randomness:
        rand_angle_r = uniform(-RAND_ANGLE_MAX, RAND_ANGLE_MAX)
        rand_factor_r = uniform(1-RAND_FACTOR_MAX, 1+RAND_FACTOR_MAX)
        rand_angle_l = uniform(-RAND_ANGLE_MAX, RAND_ANGLE_MAX)
        rand_factor_l = uniform(1-RAND_FACTOR_MAX, 1+RAND_FACTOR_MAX)

    # branch to the right
    tree.right(angle + rand_angle_r)
    branch(rand_factor_r * length / dividend, use_randomness)

    # branch to the left
    tree.goto(pos)
    tree.setheading(heading)
    tree.left(angle + rand_angle_l)
    branch(rand_factor_l * length / dividend, use_randomness)


def main():
    global angle
    use_randomness = True
    redraw = True
    while True:
        tree.goto((WIN_WIDTH/2, WIN_HEIGHT - 30))
        tree.setheading(180)

        if redraw:
            clear(wn)
            branch(100, use_randomness)
            wn.update()

        #click_point = wn.checkMouse()
        #click_point = wn.getMouse()
        #if click_point != None and click_point.x < 20 and click_point.y < 20:
        #    break

        #redraw = False

        key = wn.checkKey()
        redraw = key != None and key != '' #or key != ''

        if key == 'q':
            angle = angle + 1
        elif key == 'a':
            angle = angle - 1
        elif key == 'c':
            break

    wn.close()


main()
