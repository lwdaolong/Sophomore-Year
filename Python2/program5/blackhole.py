# The Black_Hole class is derived from Simulton; it updates by finding+removing
#   any class derived from Prey whose center is contained inside its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10

    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)

    def update(self, model):
        simultons_eaten = set()
        for simulton in model.simultons:
            if isinstance(simulton,Prey):
                if self.contains(simulton.get_location()):
                    simultons_eaten.add(simulton)
        for simulton in simultons_eaten:
            model.remove(simulton)
        return simultons_eaten

    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                           self._x + self.radius, self._y + self.radius,
                           fill='#000000')

    def contains(self,xy):
        if self.distance(xy) <= self.radius:
            return True
        return False

