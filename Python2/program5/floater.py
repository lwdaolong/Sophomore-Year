# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math


class Floater(Prey):
    radius = 5

    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 2 * math.pi * random(), 5)

    def update(self, model):
        temp_random = random()
        if temp_random <=.3:
            delta_speed = random()-.5
            delta_radian = random()-.5
            self.set_angle(self.get_angle() + delta_radian)
            if self.get_speed() + delta_speed < 3:
                self.set_speed(3)
            elif self.get_speed() + delta_speed > 7:
                self.set_speed(7)
            else:
                self.set_speed(self.get_speed() + delta_speed)
        else:
            pass
        self.move()

    def display(self, canvas):
        canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius,
                           self._x + Floater.radius, self._y + Floater.radius,
                           fill='#BE2625')

