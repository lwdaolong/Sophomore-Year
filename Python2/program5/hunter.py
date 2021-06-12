# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.

import math,random
from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    max_chase_distance = 200

    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self,x,y,20,20,2*math.pi*random.random(),5)

    def update(self, model):
        objs_eaten = super().update(model)
        self.move()

        temp_set = model.simultons
        prey_set =set()
        for obj in temp_set:
            if isinstance(obj,Prey):
                prey_set.add(obj)
        distance_list=[]
        for item in prey_set:
            distance = self.distance(item.get_location())
            if distance < self.max_chase_distance:
                distance_list.append((distance,item))
        distance_list.sort()
        if len(distance_list) > 0:
            self.set_angle(atan2(distance_list[0][1].get_location()[1]-self.get_location()[1],distance_list[0][1].get_location()[0]-self.get_location()[0]))


        return objs_eaten
