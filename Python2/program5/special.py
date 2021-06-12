# A Special is Ball; it updates by moving in a spiralling circle
#   the special object gradually gets faster and spirals out of control
#   and displays as yellow circle with a radius
#   of 5 (width/height 10).

import math,random
from ball import Ball


class Special(Ball):

    def __init__(self, x, y):
        Ball.__init__(self, x, y)

    def update(self,model):
        super().update(model)
        self.set_angle(self.get_angle()+1)
        self.set_speed(self.get_speed()+1)

    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                           self._x + self.radius, self._y + self.radius,
                           fill='#FCDC3B')