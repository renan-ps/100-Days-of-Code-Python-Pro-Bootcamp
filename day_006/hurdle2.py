def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pulo():
    while at_goal() == False:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

pulo()