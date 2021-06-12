# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter_constant = 30

    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 0

    def update(self, model):
        objs_eaten = super().update(model)
        delta_radius = len(objs_eaten)
        if delta_radius !=0:
            self.radius += delta_radius
            self.counter =0
        if self.counter >=30:
            self.radius -=1
            self.counter = 0
        if self.radius <0:
            model.remove(self)
        self.counter +=1
        return objs_eaten
