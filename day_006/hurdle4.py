def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    cont = 0
    turn_left()
    while wall_on_right():
        move()
        cont += 1
    turn_right()
    move()
    turn_right()
    while cont > 0:
        move()
        cont -= 1
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()