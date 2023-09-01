def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pulo(obstaculos):
    for n in range(1, obstaculos + 1):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

pulo(6)
    



