from graphics import *
import math

class MyTurtle:
    # :DDDDDDDDD

	_x = 0
    _y = 0
    _angle = 0

    def __init__(self, win, x, y, angle):
        self._win = win
        self._x = x
        self._y = y
        self._angle = angle

    def forward(self, length):
        # Calculate new x and y by _angle and length
        dx = math.sin(self.get_radians()) * length
        dy = math.cos(self.get_radians()) * length
        p2 = Point(self._x + dx, self._y + dy)
        line = Line(Point(self._x, self._y), p2)
        g = 0 #g = 255 - int(length * 3)
        if g < 0:
            g = 0
        line.setFill(color_rgb(0, g, 0))
        line.draw(self._win)
        self._x = p2.x
        self._y = p2.y

    def get_radians(self):
        return math.pi * self._angle / 180.0

    def pos(self):
        pos_tuple = (self._x, self._y)
        return pos_tuple

    def heading(self):
        return self._angle

    def right(self, d_angle):
        self._angle = self._angle + d_angle

    def setheading(self, heading):
        self._angle = heading

    def left(self, d_angle):
        self._angle = self._angle - d_angle

    def goto(self, pos):
        self._x, self._y = pos
