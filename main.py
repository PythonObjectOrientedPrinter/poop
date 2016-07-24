from poop.gcode import Gcode


gcodes = Gcode('test.gcode')

while gcodes.has_work():
    print("Doing work")