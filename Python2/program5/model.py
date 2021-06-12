import controller
import model   # See how update_all should pass on a reference to this module

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simultons       = set()
current_action = None #used to remember what object to add/remove


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons
    running = False
    cycle_count = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    cycle_count += 1
    for b in simultons:
        b.update(model)
    running = False



#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global current_action
    current_action = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if current_action == 'Remove':
        objs_to_remove =[]
        for simulton in simultons:
            if simulton.contains((x,y)):
                objs_to_remove.append(simulton)#code for removing clicked object from simultons
        for obj in objs_to_remove:
            remove(obj)
    else:
        if current_action in {'Ball','Floater','Black_Hole','Pulsator','Hunter','Special'}: #use eval later for easier scaling
            if current_action == 'Ball':
                simultons.add( Ball(x,y))
            elif current_action == 'Floater':
                simultons.add( Floater(x,y))
            elif current_action == 'Black_Hole':
                simultons.add( Black_Hole(x,y))
            elif current_action == 'Pulsator':
                simultons.add( Pulsator(x,y))
            elif current_action == 'Hunter':
                simultons.add( Hunter(x,y))
            elif current_action == 'Special':
                simultons.add( Special(x,y))
        else:
            pass # do nothing because not valid button to do anything on screen with

#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    s = set()
    for b in simultons:
        if p(b):
            s.add(b)
    return s


#call update for each simulton in this simulation (pass model as an argument) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    try:
        if running:
            cycle_count += 1
            for b in simultons:
                b.update(model)
    except:
        pass



#For animation: (1st) delete all simultons on the canvas; (2nd) call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; (3rd) update the label defined in the controller for progress 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)

    for b in simultons:
        b.display(controller.the_canvas)

    controller.the_progress.config(text=str(len(simultons)) + " simultons/" + str(cycle_count) + " cycles")

